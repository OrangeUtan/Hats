# Generates the item models which are used as the base for all hats.
# Each model is overwritten with custom hat models depending on the items custom model data.

import yaml, json
from registry import Registry, Hat

def minecraft_item_model_overwrite(custom_model_data, model_path):
	""" Creates a custom model overwrite for minecraft item models """
	return { "predicate": { "custom_model_data": custom_model_data }, "model": model_path }

registry = Registry()
hats = list(registry.all_hats())
overrides = [minecraft_item_model_overwrite(hat.custom_model_data, hat.model_path) for hat in sorted(hats, key=lambda hat: hat.custom_model_data)]

for key, item_model in registry.overwritten_item_models.items():
	item_model.model["overrides"] = overrides
	with open(item_model.path, "w+") as file:
		json.dump(item_model.model, file, separators=(',', ':'), indent=4)