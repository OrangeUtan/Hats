import json, os
from registry import Registry, Hat
import shutil

def hat_loot_table(hat, base_item):
	functions = [
		{
			"function": "minecraft:set_name",
			"name": {
				"translate": hat.translation
			}
		},
		{
			"function": "set_nbt",
			"tag": f'{{CustomModelData:{hat.custom_model_data}, Tags:["hats.hat", "{hat.type}"]}}'
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

def delete_folder(path: str):
	for root, dirs, files in os.walk('/path/to/folder'):
		for f in files:
			os.unlink(os.path.join(root, f))
		for d in dirs:
			shutil.rmtree(os.path.join(root, d))

registry = Registry()
hats = list(registry.all_hats())

delete_folder("datapack/data/hats/loot_tables/hat")
delete_folder("datapack/data/hats/loot_tables/hat_on_head")

for hat in hats:
	if hat.category == "*":
		rel_path = f"{hat.name}"
	else:
		rel_path = f"{hat.category}/{hat.name}"

	hat_loot_table_dir = f"datapack/data/hats/loot_tables/hat/{hat.category}"
	if not os.path.exists(hat_loot_table_dir):
		os.makedirs(hat_loot_table_dir)

	hat_loot_table_path = f"datapack/data/hats/loot_tables/hat/{rel_path}.json"
	
	with open(hat_loot_table_path, "w+") as file:
		json.dump(hat_loot_table(hat, "hats:hat"), file, separators=(',', ':'), indent=4)

	hat_on_head_loot_table_path = f"datapack/data/hats/loot_tables/hat_on_head/{rel_path}.json"
	with open(hat_on_head_loot_table_path, "w+") as file:
		json.dump(hat_loot_table(hat, "hats:hat_on_head"), file, separators=(',', ':'), indent=4)