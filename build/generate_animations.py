import os, yaml
import json as JSON
from dataclasses import dataclass
from fractions import Fraction

@dataclass
class State:
	name: str
	index: int

	@classmethod
	def from_json(cls, name, json):
		return State(name, json["index"])

@dataclass
class Sequence:
	name: str
	entries: list

	is_weighted: bool
	total_weight: int

	@classmethod
	def from_json(cls, name, json):
		
		# Collect some initial information about the entries
		is_weighted = False
		total_weight = 0
		for entry in json:
			if "weight" in entry:
				is_weighted = True
				total_weight += entry["weight"]

		return Sequence(name, json, is_weighted, total_weight)

	def to_frames(self, states, sequences, duration=None):
		if self.is_weighted:
			converted = self._convert_entries_weighted(states, sequences, duration)
		else:
			converted = self._convert_entries_abs_time(states, sequences)

		return list(self._combine_consecutive_frames(converted))

	def _convert_entries_abs_time(self, states, sequences):
		for entry in self.entries:
			type, ref, repeat = entry["type"], entry["ref"], max(1,entry.get("repeat", 1))

			if type == "state":
				# Get the frame index
				if not ref in states:
					raise Exception(f"State '{ref}' doesn't exist")
				index = states[ref].index

				time = entry.get("duration", 1)
				yield self._frame(index, time*repeat)
			
			elif type == "sequence":
				if not ref in sequences:
					raise Exception(f"Sequence '{ref}' doesn't exist")
				referenced_sequence = sequences[ref]

				seq_duration = entry.get("duration", None)

				seq_frames = referenced_sequence.to_frames(states, sequences, seq_duration)
				for i in range(repeat):
					for frame in seq_frames:
						yield frame.copy()

	def _convert_entries_weighted(self, states, sequences, duration):
		if self.is_weighted and not duration:
			raise Exception("Parameter 'duration' missing")

		fixed_duration = self._calc_fixed_duration(sequences)
		duration -= fixed_duration

		frames = []
		remaining_duration = duration
		for entry in self.entries:
			type, ref, repeat = entry["type"], entry["ref"], max(1,entry.get("repeat", 1))

			if type == "state":
				# Get the frame index
				if not ref in states:
					raise Exception(f"State '{ref}' doesn't exist")
				index = states[ref].index

				if not "weight" in entry:
					frames.append(self._frame(index, entry.get("duration", 1)*repeat))
				else:
					time = self._calc_weighted_time(index, entry.get("weight", 1), duration, remaining_duration)
					remaining_duration -= time
					frames.append(self._frame(index, time*repeat))

			elif type == "sequence":
				# Get the referenced sequence
				if not ref in sequences:
					raise Exception(f"Sequence '{ref}' doesn't exist")
				referenced_sequence = sequences[ref]

				for i in range(repeat):
					if not referenced_sequence.is_weighted:
						frames += referenced_sequence.to_frames(states, sequences)
					else:
						seq_duration = self._calc_weighted_time(index, entry.get("weight", 1)/repeat, duration, remaining_duration)
						remaining_duration -= seq_duration
						frames += referenced_sequence.to_frames(states, sequences, seq_duration)

		if remaining_duration < 0:
			raise Exception("Something went wrong when calculating weighted time")

		# TODO changes duration of fixed duration states
		if remaining_duration > 0:
			for i in range(remaining_duration):
				frames[i]["time"] += 1

		return frames

	def _calc_fixed_duration(self, sequences):
		fixed_duration = 0
		for entry in self.entries:
			type, ref, repeat = entry["type"], entry["ref"], max(1,entry.get("repeat", 1))

			if type == "state":
				if not "weight" in entry:
					fixed_duration += entry.get("duration", 1)*repeat
			elif type == "sequence":
				if not ref in sequences:
					raise Exception(f"Sequence '{ref}' doesn't exist")
				referenced_sequence = sequences[ref]

				if referenced_sequence.is_weighted:
					fixed_duration += referenced_sequence.get("duration", 1)
				else:
					fixed_duration += referenced_sequence._calc_fixed_duration(sequences)*repeat

		return fixed_duration

	@classmethod
	def _frame(cls, index, time):
		return {"index": index, "time": time}

	def _calc_weighted_time(self, index, weight, duration, remaining_duration):
		weighted_time = int((weight*duration)/self.total_weight) # Calculate time based on weight
		return max(1,min(remaining_duration, weighted_time)) # Assure that: 1 <= time <= remaining_time

	@classmethod
	def _combine_consecutive_frames(cls, frames):
		prev_frame = None
		for frame in frames:
			if prev_frame:
				if prev_frame["index"] == frame["index"]:
					prev_frame["time"] += frame["time"]
				else:
					yield prev_frame
					prev_frame = frame
			else:
				prev_frame = frame

		if prev_frame:
			yield prev_frame
			
	
@dataclass
class Animation:
	out_file: str
	states: list
	sequences: list
	interpolate: bool
	frametime: int

	@classmethod
	def from_json(cls, json):
		out_file = f"resourcepack/assets/minecraft/textures/{json['texture']}.mcmeta"

		states = dict()
		for name, state_json in json["states"].items():
			states[name] = State.from_json(name, state_json)

		sequences = dict()
		for name, sequence_json in json["sequences"].items():
			sequences[name] = Sequence.from_json(name, sequence_json)

		# Check if root sequence meets requirements
		if not "root" in sequences:
			raise Exception("Animation must contain a root sequence")
		if sequences["root"].is_weighted:
			raise Exception("Root sequence can't be weighted")

		return Animation(out_file, states, sequences, json.get("interpolate", False), json.get("frametime", 1))

	def to_animation(self):
		return {
			"animation": {
				"interpolate": self.interpolate,
				"frametime": self.frametime,
				"frames": self.sequences["root"].to_frames(self.states, self.sequences)
			}
		}

def generate_animation_file(path):
	json = load_yaml_file(path)
	animation = Animation.from_json(json)

	with open(animation.out_file, "w+") as file:
		JSON.dump(animation.to_animation(), file, indent=4)

def load_yaml_file(path):
	with open(path) as file:
		return yaml.load(file, Loader=yaml.Loader)

for root, dirs, files in os.walk("animations"):
	for file in files:
		if os.path.splitext(file)[1] == ".yml":
			path = os.path.join(root, file)
			generate_animation_file(path)