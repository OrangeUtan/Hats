import os, yaml, json
from ModelAnimation import *

def generate_model_animation(path):
	data = load_yaml_file(path)
	modelAnim = ModelAnimation.from_json(data)

	for textureAnimation in modelAnim.textureAnimations:
		with open(textureAnimation.out_file, "w+") as file:
			anim = textureAnimation.to_animation()
			num_frames = sum(map(lambda frame: frame['time'], anim['animation']['frames']))
			print(f"{textureAnimation.out_file} -> {num_frames} frames")
			json.dump(anim, file, indent=4)

def load_yaml_file(path):
	with open(path) as file:
		return yaml.load(file, Loader=yaml.Loader)

for root, dirs, files in os.walk("animations"):
	for file in files:
		if os.path.splitext(file)[1] == ".yml":
			path = os.path.join(root, file)
			generate_model_animation(path)