import inspect, os
from registry import Registry, Hat

registry = Registry()
hats = list(registry.all_hats())
base_item_on_head = "stick"

for hat in hats:
	if hat.category == "*":
		rel_path = f"{hat.name}"
	else:
		rel_path = f"{hat.category}/{hat.name}"
		
	function_path = f"datapack/data/hats/functions/fix_hat/{rel_path}.mcfunction"
	function_content = inspect.cleandoc(f"""
		# as: Player, descr: Replace #hat item with equivalent #hat_on_head item
		clear @s minecraft:{base_item_on_head}{{CustomModelData:{hat.custom_model_data}, Tags:["is_hat"]}} 1
		execute as @s run loot give @s loot hats:hat/{rel_path}
		""")

	parent_dir = os.path.split(function_path)[0]
	if not os.path.exists(parent_dir):
		os.makedirs(parent_dir)

	with open(function_path, "w") as file:
		file.write(function_content)