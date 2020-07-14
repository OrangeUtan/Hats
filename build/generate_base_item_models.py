# Generates the item models which are used as the base for all hats.
# Each model is overwritten with custom hat models depending on the items custom model data.

import yaml, json
from registry import Registry, Hat

def minecraft_item_model_overwrite(custom_model_data, model_path):
	""" Creates a custom model overwrite for minecraft item models """
	return { "predicate": { "custom_model_data": custom_model_data }, "model": model_path }

registry = Registry()

item_name_to_overrides_map = dict(map(lambda i: (i, []),registry.items))
for _, hat in sorted(registry.cmd_to_hat_map.items(), key=lambda x: x[0]):
	item_inv = registry.get_item_inv(hat.item_inv)
	item_on_head = registry.get_item_on_head(hat.item_on_head)
	
	override = minecraft_item_model_overwrite(hat.custom_model_data, hat.model_path)
	item_name_to_overrides_map[item_inv.name].append(override)
	item_name_to_overrides_map[item_on_head.name].append(override)

for item_name, overrides in item_name_to_overrides_map.items():
	if len(overrides) < 1:
		continue
 
	item = registry.items[item_name]
	item.model["overrides"] = overrides

	with open(item.model_path, "w+") as file:
		json.dump(item.model, file, separators=(',', ':'), indent=4)