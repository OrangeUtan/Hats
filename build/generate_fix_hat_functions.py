import inspect, os
from registry import Registry, Hat

def generate_fix_hat_functions(hats):
	for hat in hats:
		if hat.category == "*":
			rel_path = f"{hat.name}"
		else:
			rel_path = f"{hat.category}/{hat.name}"
			
		function_path = f"datapack/data/hats/functions/fix_hat/{rel_path}.mcfunction"
		function_content = inspect.cleandoc(f"""
			# as: Player, descr: Replace #hat item with equivalent #hat_on_head item
			clear @s {base_item_on_head}{{CustomModelData:{hat.custom_model_data}, Tags:["is_hat"]}} 1
			execute as @s run loot give @s loot hats:hat/{rel_path}
			""")

		parent_dir = os.path.split(function_path)[0]
		if not os.path.exists(parent_dir):
			os.makedirs(parent_dir)

		with open(function_path, "w") as file:
			file.write(function_content)

def generate_root_function(hats):
	function_content = inspect.cleandoc("""
		# as: Player
		# descr: When a Player takes of their hat, they have #hat_on_head item in their inventory.
		#        Replace that item with an equivalent #hat item""")
	function_content += "\n"

	for hat in hats:
		if hat.category == "*":
			rel_path = f"{hat.name}"
		else:
			rel_path = f"{hat.category}/{hat.name}"

		function_content += "\n"
		conditional_command = f"execute as @s[nbt={{Inventory:[{{id:\"{base_item_on_head}\",tag:{{Tags:[\"is_hat\"],CustomModelData:{hat.custom_model_data}}}}}]}}] run function hats:fix_hat/{rel_path}"
		function_content += conditional_command

	function_path = "datapack/data/hats/functions/hat_behavior/fix_hat_from_head.mcfunction"
	parent_dir = os.path.split(function_path)[0]
	if not os.path.exists(parent_dir):
		os.makedirs(parent_dir)

	with open(function_path, "w+") as file:
		file.write(function_content)

registry = Registry()
hats = list(registry.all_hats())
base_item_on_head = "minecraft:stick"

generate_fix_hat_functions(hats)
generate_root_function(hats)
