import os, yaml
from ModelAnimation import *

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