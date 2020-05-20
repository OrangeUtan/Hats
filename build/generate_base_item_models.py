# Generates the item models which are used as the base for all hats.
# Each model is overwritten with custom hat models depending on the items custom model data.

import yaml, json
from registry import Registry, Hat

def minecraft_item_model_overwrite(custom_model_data, model_path):
	""" Creates a custom model overwrite for minecraft item models """
	return { "predicate": { "custom_model_data": custom_model_data }, "model": model_path }

def minecraft_item_model(base_model, overrides=None):
	""" Creates a minecraft item model """
	if overrides:
		base_model['overrides'] = overrides
	return base_model

registry = Registry()
hats = list(registry.all_hats())
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