import os, yaml, json
from dataclasses import dataclass
from fractions import Fraction

@dataclass
class Frame:
	name: str
	index: int

	@classmethod
	def from_json(cls, name, json):
		return Frame(name, json["index"])
	
@dataclass
class Sequence:
	name: str
	total_weight: int
	frame_references: list

	@classmethod
	def from_json(cls, name, json):

		total_weight = 0
		for frame in json:
			total_weight += frame.get("weight", 0)

		return Sequence(name, total_weight, json)

	def generate_frames(self, duration, frames_dict):
		gen_frames = []
		used_duration = 0
		for ref in self.frame_references:
			frame_ref, weight, time = ref["frame"], ref.get("weight",1), ref.get("time",0)

			if time == 0:
				time = max(1,int(weight*duration/self.total_weight))
				
			used_duration += time
			gen_frames.append({
				"index": frames_dict[frame_ref].index,
				"time": time
			})

		# Distribute left over time
		if duration-used_duration > 0:
			for i in range(duration-used_duration):
				gen_frames[i]["time"] += 1

		return gen_frames

def create_json_animation(animation, frames_dict, sequences_dict, interpolate=False, frametime=1):
	frames = []
	for entry in animation:
		type, ref, duration, repeat = entry.get("type", "frame"), entry["ref"], entry.get("duration", 1), entry.get("repeat", 1)
		
		if type == "sequence":
			seq_frames = sequences_dict[ref].generate_frames(duration, frames_dict)
			for i in range(repeat):
				if len(frames) > 0 and frames[-1]["index"] == seq_frames[0]["index"]:
					frames[-1]["time"] += seq_frames[0]["time"]
					del seq_frames[-1]
				frames += seq_frames
		elif type == "frame":
			frame = {
				"index": frames_dict[ref].index,
				"time": max(1,duration)
			}
			for i in range(repeat):
				if len(frames) > 0 and frames[-1]["index"] == frame["index"]:
					frames[-1]["time"] += frame["time"]
				else:
					frames.append(frame)

	return {
		"animation": {
			"interpolate": interpolate,
			"frametime": frametime,
			"frames": frames
		}
	}

def generate_animation_file(path):
	anim_file = load_yaml_file(path)
	out = f"resourcepack/assets/minecraft/textures/{anim_file['texture']}.mcmeta"

	frames_dict = dict()
	for name, data in anim_file["frames"].items():
		frames_dict[name] = Frame.from_json(name, data)

	sequences_dict = dict()
	for name, data in anim_file["sequences"].items():
		sequences_dict[name] = Sequence.from_json(name, data)

	anim = create_json_animation(anim_file["animation"], frames_dict, sequences_dict)

	with open(out, "w+") as file:
		json.dump(anim, file, indent=4)

def load_yaml_file(path):
	with open(path) as file:
		return yaml.load(file, Loader=yaml.Loader)

for root, dirs, files in os.walk("animations"):
	for file in files:
		if os.path.splitext(file)[1] == ".yml":
			path = os.path.join(root, file)
			generate_animation_file(path)