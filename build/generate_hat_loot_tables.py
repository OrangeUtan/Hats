import json, os
from registry import Registry, Hat

def hat_loot_table(hat, base_item):
	if hat.category == "*":
		translation = f"{hat.name}"
	else:
		translation = f"{hat.category}.{hat.name}"

	functions = [
		{
			"function": "minecraft:set_name",
			"name": {
				"translate": f"item.hats.{translation}.name"
			}
		},
		{
			"function": "set_nbt",
			"tag": f'{{CustomModelData:{hat.custom_model_data}, Tags:["is_hat", "hats.hat", "{hat.type}"]}}'
		}
	]

	# Add lore lines if any exist
	if hat.lore:
		lines = [{"translate": f"{line}"} for line in hat.lore]
		functions.append({
			"function": "minecraft:set_lore",
			"lore": lines
		})

	return {
    	"type": "minecraft:generic",
   		"pools": [
			{
				"functions": functions,
				"rolls": 1,
				"entries": [
					{
						"type": "tag",
						"name": base_item,
						"expand": True
					}
				]
			}
		]
	}

registry = Registry()
hats = list(registry.all_hats())

for hat in hats:
	if hat.category == "*":
		rel_path = f"{hat.name}"
	else:
		rel_path = f"{hat.category}/{hat.name}"

	hat_loot_table_path = f"datapack/data/hats/loot_tables/hat/{rel_path}.json"
	with open(hat_loot_table_path, "w+") as file:
		json.dump(hat_loot_table(hat, "hats:hat"), file, separators=(',', ':'), indent=4)

	hat_on_head_loot_table_path = f"datapack/data/hats/loot_tables/hat_on_head/{rel_path}.json"
	with open(hat_on_head_loot_table_path, "w+") as file:
		json.dump(hat_loot_table(hat, "hats:hat_on_head"), file, separators=(',', ':'), indent=4)