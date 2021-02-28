from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

import yaml


@dataclass
class Registry:
    custom_model_data_id: int
    items: dict[str, Item]
    default_item_inv: str
    default_item_on_head: str
    categories: dict[str, list[Hat]]
    cmd_to_hat_map: dict[int, Hat]

    @classmethod
    def from_json(cls):
        json = load_yaml_file("hat_registry.yml")

        custom_model_data_id = json["cmd_id"]

        # Parse categories
        cmd_to_hat_map = {}
        categories = {}
        for category_name, category_hats in json["hats"].items():
            hats = []
            for hat_name, hat_json in category_hats.items():
                hat = Hat.from_json(hat_name, category_name, custom_model_data_id, hat_json)

                if hat.custom_model_data in cmd_to_hat_map:
                    raise Exception(
                        f"Can't add {hat}, Custom Model Data {cmd_to_hat_map[hat.custom_model_data]} already has the same Custom Model Data"
                    )

                cmd_to_hat_map[hat.custom_model_data] = hat
                hats.append(hat)

            categories[category_name] = hats

        return cls(
            custom_model_data_id,
            {name: Item.from_json(name, data) for name, data in json["items"].items()},
            json["default_item_inv"],
            json["default_item_on_head"],
            categories,
            cmd_to_hat_map,
        )

    def __post_init__(self):
        self.namespace = "oran9eutan"
        self.datapack_name = "hats"
        self.advancement_dir = (
            f"datapack/data/{self.namespace}/advancements/{self.datapack_name}"
        )
        self.functions_dir = f"datapack/data/{self.namespace}/functions/{self.datapack_name}"
        self.loot_tables_dir = (
            f"datapack/data/{self.namespace}/loot_tables/{self.datapack_name}"
        )
        self.predicates_dir = f"datapack/data/{self.namespace}/predicates/{self.datapack_name}"

    def all_hats(self):
        for category_name, category_hats in self.categories.items():
            for hat in category_hats:
                yield hat

    def get_item_inv(self, name: str):
        if not name in self.items:
            return self.items[self.default_item_inv]
        else:
            return self.items[name]

    def get_item_on_head(self, name: str):
        if not name in self.items:
            return self.items[self.default_item_on_head]
        else:
            return self.items[name]


@dataclass
class Item:
    name: str
    id: str
    model_path: str
    model: dict

    @classmethod
    def from_json(cls, name, json):
        id = json["id"]
        if id.startswith("minecraft"):
            id = id[len("minecraft:") :]
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

    item_inv: str
    item_on_head: str

    @classmethod
    def from_json(cls, name: str, category: str, cmd_id: int, json: Dict):
        categorized_name = f"{category}{{0}}{name}"

        cmd = cmd_id * 10000 + json["cmd"]

        model_path = f"item/hats/{json.get('model', categorized_name.format('/'))}"
        type = f"hats.hat.type.{json['type']}"
        translation = f"item.hats.hat.{json['type']}.name"

        lore = None
        if "num_lore_lines" in json:
            lore = [
                f"item.hats.hat.{json['type']}.lore{i+1}"
                for i in range(json.get("num_lore_lines", 0))
            ]

        return Hat(
            name,
            category,
            cmd,
            model_path,
            type,
            translation,
            lore,
            json.get("item_inv"),
            json.get("item_on_head"),
        )


def load_yaml_file(path):
    with open(path) as file:
        return yaml.load(file, Loader=yaml.Loader)
