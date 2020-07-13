from __future__ import annotations
import yaml
from dataclasses import dataclass
from typing import Dict

class Registry:
	def __init__(self):
		self.load("hat_registry.yml")
		
	def all_hats(self):
		for category_name, category_hats in self.categories.items():
			for hat in category_hats:
				yield hat

	def load(self, path: str):
		json = load_yaml_file("hat_registry.yml")
		self.overwritten_item_models = dict(map(lambda i: (i[0], Item.from_json(i[0], i[1])), json["items"].items()))
		self.categories = Registry._parse_categories(json)

	@classmethod
	def _parse_categories(cls, registry):
		categories = dict()
		for category_name, category_hats in map(lambda c: c , registry["hats"].items()):
			hats = list(map(lambda h: Hat.from_json(h[0], category_name, h[1]), category_hats.items()))
			categories[category_name] = hats
		return categories

@dataclass
class Item:
	name: str
	id: str
	path: str
	model: dict

	@classmethod
	def from_json(cls, name, json):
		id = json["id"]
		if id.startswith("minecraft"):
			id = id[len("minecraft:"):]
		path = f"resourcepack/assets/minecraft/models/item/{id}.json"
		return Item(name, id, path, json["model"])
		
@dataclass
class Hat:
	name: str
	category: str
	custom_model_data: int
	model_path: str
	type: str
	translation: str
	lore: list

	@classmethod
	def from_json(cls, name:str, category: str, json: Dict):
		categorized_name = f"{category}{{0}}{name}"

		model_path = f"item/hats/{json.get('model', categorized_name.format('/'))}"
		type = f"hats.hat.type.{json['type']}"
		translation = f"item.hats.hat.{json['type']}.name"

		lore = None
		if "num_lore_lines" in json:
			lore = [f"item.hats.hat.{json['type']}.lore{i+1}" for i in range(json.get("num_lore_lines", 0))]

		return Hat(name, category, json["cmd"], model_path, type, translation, lore)

def load_yaml_file(path):
	with open(path) as file:
		return yaml.load(file, Loader=yaml.Loader)