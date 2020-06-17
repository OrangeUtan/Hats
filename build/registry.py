import yaml
from dataclasses import dataclass

class Registry:
	def __init__(self):
		self.registry = load_yaml_file("hat_registry.yml")
		self.overwritten_item_models = Registry._parse_root_items(self.registry)
		self.categories = Registry._parse_categories(self.registry)
		
	def all_hats(self):
		for category_name, category_hats in self.categories.items():
			for hat in category_hats:
				yield hat

	# def categories(self):
	# 	for category_name, category_hats in map(lambda category: list(category.items())[0], self.registry['categories']):
	# 		hats = list(self._parse_hats(category_name, category_hats))
	# 		yield (category_name, hats)

	@classmethod
	def _parse_categories(cls, registry):
		categories = dict()
		for category_name, category_hats in map(lambda category: list(category.items())[0], registry['categories']):
			hats = list(Registry._parse_hats(category_name, category_hats))
			categories[category_name] = hats
		return categories

	@classmethod
	def _parse_hats(cls, category_name, json_hats):
		for hat_name, hat_data in map(lambda category_entry: list(category_entry.items())[0], json_hats):
			if category_name == "*":
				categorized_name = f"{hat_name}"
			else:
				categorized_name = f"{category_name}{{0}}{hat_name}"
			
			custom_model_data = hat_data['custom_model_data']
			model = f"item/hats/{hat_data.get('model', categorized_name.format('/'))}"
			type = f"hats.hat.type.{categorized_name.format('.')}"
			translation = f"item.hats.{categorized_name.format('.')}"
			
			lore = None
			if "num_lore_lines" in hat_data:
				lore = [f"item.hats.{categorized_name.format('.')}.lore{i+1}" for i in range(hat_data.get("num_lore_lines", 0))]
				
			yield Hat(hat_name, category_name, custom_model_data, model, type, translation, lore)

	@classmethod
	def _parse_root_items(cls, registry):
		root_items = dict()
		for key, val in registry["overwritten-item-models"].items():
			id = val["id"]
			if id.startswith("minecraft"):
				id = id[len("minecraft:"):]
			root_items.update({key:ItemModel(val["id"], f"resourcepack/assets/minecraft/models/item/{id}.json", val["model"])})
		return root_items

@dataclass
class ItemModel:
	id: str
	path: str
	model: dict
		
@dataclass
class Hat:
	name: str
	category: str
	custom_model_data: int
	model_path: str
	type: str
	translation: str
	lore: list

def load_yaml_file(path):
	with open(path) as file:
		return yaml.load(file, Loader=yaml.Loader)