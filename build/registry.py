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

	def categories(self):
		for category_name, category_hats in map(lambda category: list(category.items())[0], self.registry['categories']):
			hats = list(self._parse_hats(category_name, category_hats))
			yield (category_name, hats)

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

def load_yaml_file(path):
	with open(path) as file:
		return yaml.load(file, Loader=yaml.Loader)