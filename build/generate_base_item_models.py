# Generates the item models which are used as the base for all hats.
# Each model is overwritten with custom hat models depending on the items custom model data.

import yaml, json
from dataclasses import dataclass

@dataclass
class Hat:
	name: str
	category: str
	custom_model_data: int
	model_path: str
	type: str
	translation: str

def load_yaml_file(path):
	with open(path) as file:
		return yaml.load(file, Loader=yaml.Loader)

def hats_from_categories(categories):
	""" Takes a list of category dicts each with a list of hat dicts and converts it to one list of hats """
	for category_name, category_hats in map(lambda category: list(category.items())[0], categories):
		for hat_name, hat_data in map(lambda category_entry: list(category_entry.items())[0], category_hats):
			custom_model_data = hat_data['custom_model_data']
			
			if category_name == "*":
				# Category "*" contains all uncategorized hats -> don't add a category to any paths
				model = f"item/hats/{hat_name}"
				type = f"hats.hat.type.{hat_name}"
				translation = f"item.hats.{hat_name}"
			else:
				model = f"item/hats/{category_name}/{hat_name}"
				type = f"hats.hat.type.{category_name}.{hat_name}"
				translation = f"item.hats.{category_name}.{hat_name}"
			yield Hat(hat_name, category_name, custom_model_data, model, type, translation)

def minecraft_item_model_overwrite(custom_model_data, model_path):
	""" Creates a custom model overwrite for minecraft item models """
	return { "predicate": { "custom_model_data": custom_model_data }, "model": model_path }

def minecraft_item_model(base_model, overrides=None):
	""" Creates a minecraft item model """
	if overrides:
		base_model['overrides'] = overrides
	return base_model

registry = load_yaml_file("hat_registry.yml")
hats = list(hats_from_categories(registry['categories']))
overrides = [minecraft_item_model_overwrite(hat.custom_model_data, hat.model_path) for hat in hats]

# Create item model for hats
with open("resourcepack/assets/minecraft/models/item/leather_helmet.json", "w+") as file:
	leather_helmet = minecraft_item_model({
		"parent": "item/generated",
		"textures": {
			"layer0": "item/leather_helmet",
			"layer1": "item/leather_helmet_overlay"
		}
	}, overrides)
	json.dump(leather_helmet, file, separators=(',', ':'))

# Create item model for hats on entities heads
with open("resourcepack/assets/minecraft/models/item/stick.json", "w+") as file:
	stick = minecraft_item_model({
		"parent": "item/handheld",
		"textures": {
			"layer0": "item/stick"
		}
	}, overrides)
	json.dump(stick, file, separators=(',', ':'))