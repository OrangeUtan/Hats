import os
import json as JSON
from dataclasses import dataclass
from fractions import Fraction
from enum import Enum

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
		entries = []
		for entry in map(lambda entry: ReferenceEntry.from_json(entry), json):
			entries.append(entry)
			if entry.weight:
				is_weighted = True
				total_weight += entry.weight

		return Sequence(name, entries, is_weighted, total_weight)

	def to_frames(self, states, sequences, duration=None):
		if self.is_weighted:
			converted = self._convert_entries_weighted(states, sequences, duration)
		else:
			converted = self._convert_entries_abs_time(states, sequences)

		return list(self._combine_consecutive_frames(converted))

	def _convert_entries_abs_time(self, states, sequences):
		for entry in self.entries:
			entry.check_is_valid_reference(states, sequences)

			if entry.type == ReferenceType.STATE:
				index = states[entry.ref].index
				time = entry.duration
				yield self._frame(index, time*entry.repeat)
			
			elif entry.type == ReferenceType.SEQUENCE:
				referenced_sequence = sequences[entry.ref]
				seq_duration = entry.duration

				seq_frames = referenced_sequence.to_frames(states, sequences, seq_duration)
				for i in range(entry.repeat):
					for frame in seq_frames:
						yield frame.copy()

	def _convert_entries_weighted(self, states, sequences, duration):
		if self.is_weighted and not duration:
			raise Exception(f"Didn't pass duration to weighted sequence '{self.name}'")

		fixed_duration = self._calc_fixed_duration(sequences)
		if duration <= fixed_duration:
			raise Exception(f"Duration passed to weighted sequence {self.name} is smaller than its fixed duration")

		duration -= fixed_duration

		frames = []
		remaining_duration = duration
		for i, entry in enumerate(self.entries):
			entry.check_is_valid_reference(states, sequences)

			if entry.type == ReferenceType.STATE:
				index = states[entry.ref].index

				if entry.is_weighted(sequences):
					if remaining_duration <= 0:
						raise Exception(f"Duration is exhausted. Can't fit {i+1}. entry '{entry.ref}'")

					state_duration = entry.calc_weighted_duration(self.total_weight, duration)
					state_duration = max(1,min(remaining_duration, state_duration))
					remaining_duration -= state_duration
					frames.append(self._frame(index, state_duration))
				else:
					frames.append(self._frame(index, entry.duration))

			elif entry.type == ReferenceType.SEQUENCE:
				referenced_sequence = sequences[entry.ref]

				for i in range(entry.repeat):
					if not referenced_sequence.is_weighted:
						frames += referenced_sequence.to_frames(states, sequences)
					else:
						seq_duration = entry.weighted_duration(total_weight, duration)
						seq_duration = max(1,min(remaining_duration, seq_duration))
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
		return sum(map(lambda entry: entry.calc_fixed_duration(sequences), self.entries))

	@classmethod
	def _frame(cls, index, time):
		return {"index": index, "time": time}

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
			
class ReferenceType(Enum):
	STATE = 1
	SEQUENCE = 2

	@classmethod
	def from_string(cls,str):
		if str == "state":
			return ReferenceType.STATE
		elif str == "sequence":
			return ReferenceType.SEQUENCE

class ReferenceEntry:

	def __init__(self, type, reference, repeat, weight=None, duration=None):
		self.type = type
		self.ref = reference
		self.repeat = repeat
		self.weight = weight
		self.duration = duration

	@classmethod 
	def from_json(cls, json):
		type = ReferenceType.from_string(json["type"])
		ref = json["ref"]
		repeat = max(1, json.get("repeat",1)) # Repeat at least once
		weight = json.get("weight")
		duration = json.get("duration")

		return ReferenceEntry(type, ref, repeat, weight, duration)

	def check_is_valid_reference(self, states, sequences):
		if self.type == ReferenceType.STATE and not self.ref in states:
			raise Exception(f"State '{self.ref}' doesn't exist")
		elif self.type == ReferenceType.SEQUENCE and not self.ref in sequences:
			raise Exception(f"Sequence '{self.ref}' doesn't exist")

	def is_weighted(self, sequences):
		if self.type == ReferenceType.STATE:
			return self.weight
		elif self.type == ReferenceType.SEQUENCE:
			if self.weight:
				return True
			else:
				return sequences[ref].is_weighted

	def calc_fixed_duration(self, sequences):
		fixed_duration = 0
		if self.type == ReferenceType.STATE:
			if not self.is_weighted(sequences):
				fixed_duration = self.duration*self.repeat
		elif self.type == ReferenceType.SEQUENCE:
			referenced_sequence = sequences[self.ref]

			if referenced_sequence.is_weighted:
				fixed_duration = referenced_sequence.get("duration", 1)
			else:
				fixed_duration = referenced_sequence._calc_fixed_duration(sequences)*self.repeat
		return fixed_duration

	def calc_weighted_duration(self, total_weight, total_duration):
		if self.type == ReferenceType.STATE:
			# Ignore repeat
			return int((self.weight*total_duration)/total_weight) # Calculate duration based on weight
		elif self.type == ReferenceType.SEQUENCE:
			return int(((self.weight/self.repeat)*total_duration)/total_weight) # Calculate duration based on weight
	
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
