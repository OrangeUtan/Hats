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
		has_abs_time_entries = False
		has_weighted_entries = False
		total_weight = 0
		for entry in json:
			if "weight" in entry:
				has_weighted_entries = True
				total_weight += entry["weight"]
			if "duration" in entry:
				has_abs_time_entries = True

			if has_abs_time_entries and has_weighted_entries:
				raise Exception("Sequence can only contain entries of one type: weighted or absoulte duration")

		return Sequence(name, json, has_weighted_entries, total_weight)

	def to_frames(self, states, sequences, duration=None):
		if self.is_weighted:
			converted = self._convert_entries_weighted(states, sequences, duration)
		else:
			converted = self._convert_entries_abs_time(states, sequences)

		return list(self._combine_consecutive_frames(converted))

	def _convert_entries_abs_time(self, states, sequences):
		for entry in self.entries:
			type, ref = entry["type"], entry["ref"]

			if type == "state":
				# Get the frame index
				if not ref in states:
					raise Exception(f"State '{ref}' doesn't exist")
				index = states[ref].index

				time = entry.get("duration", 1)
				yield self._frame(index, time)
			
			elif type == "sequence":
				if not ref in sequences:
					raise Exception(f"Sequence '{ref}' doesn't exist")
				referenced_sequence = sequences[ref]

				seq_duration = entry.get("duration", None)

				for frame in referenced_sequence.to_frames(states, sequences, seq_duration):
					for i in range(max(1,entry.get("repeat", 1))):
						yield frame.copy()

	def _convert_entries_weighted(self, states, sequences, duration):
		if self.is_weighted and not duration:
			raise Exception("Parameter 'duration' missing")

		frames = []
		remaining_duration = duration
		for entry in self.entries:
			type, ref = entry["type"], entry["ref"]

			if type == "state":
				# Get the frame index
				if not ref in states:
					raise Exception(f"State '{ref}' doesn't exist")
				index = states[ref].index

				time = self._calc_weighted_time(index, entry.get("weight", 1), duration, remaining_duration)
				remaining_duration -= time

				# Add frame
				frames.append(self._frame(index, time))

			elif type == "sequence":
				# Get the referenced sequence
				if not ref in sequences:
					raise Exception(f"Sequence '{ref}' doesn't exist")
				referenced_sequence = sequences[ref]
				if not referenced_sequence.is_weighted:
					raise Exception("Weighted sequences cannot contain unweighted sequence")

				seq_duration = self._calc_weighted_time(index, entry.get("weight", 1), duration, remaining_duration)
				remaining_duration -= seq_duration

				# Add frames
				for frame in referenced_sequence.to_frames(states, sequences, seq_duration):
					for i in range(max(1,entry.get("repeat", 1))):
						frames.append(frame.copy())

		if remaining_duration < 0:
			raise Exception("Something went wrong when calculating weighted time")

		if remaining_duration > 0:
			for i in range(remaining_duration):
				frames[i]["time"] += 1

		return frames

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

		return Animation(out_file, states, sequences)

	def to_frames(self):
		return self.sequences["root"].to_frames()

def generate_animation_file(path):
	json = load_yaml_file(path)
	anim = Animation.from_json(json)

	# print(anim.states)
	# print(anim.sequences)
	# print(anim.sequences["root"])

	# anim.to_frames()
	frames = anim.sequences["test"].to_frames(anim.states, anim.sequences, 100)
	print(frames)

	# anim = create_json_animation(anim_file["animation"], frames_dict, sequences_dict)

	# with open(out, "w+") as file:
	# 	json.dump(anim, file, indent=4)

def load_yaml_file(path):
	with open(path) as file:
		return yaml.load(file, Loader=yaml.Loader)

# for root, dirs, files in os.walk("animations"):
# 	for file in files:
# 		if os.path.splitext(file)[1] == ".yml":
# 			path = os.path.join(root, file)
# 			generate_animation_file(path)

generate_animation_file("animations/dog_head.yml")