import yaml
from dataclasses import dataclass

class Registry:
	def __init__(self):
		self.registry = load_yaml_file("hat_registry.yml")

	def all_hats(self):
		for category_name, category_hats in map(lambda category: list(category.items())[0], self.registry['categories']):
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