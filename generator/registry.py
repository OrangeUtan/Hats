from __future__ import annotations
import yaml
from dataclasses import dataclass
from typing import Dict
import argparse, sys


class Registry:
    def __init__(self):
        self.load("hat_registry.yml")

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

    def load(self, path: str):
        json = load_yaml_file("hat_registry.yml")

        self.custom_model_data_id = json["cmd_id"]
        self.default_item_inv = json["default_item_inv"]
        self.default_item_on_head = json["default_item_on_head"]

        # Parse items
        self.items = dict(
            map(lambda i: (i[0], Item.from_json(i[0], i[1])), json["items"].items())
        )

        # Parse categories
        self.cmd_to_hat_map = {}
        self.categories = {}
        for category_name, category_hats in json["hats"].items():
            hats = []
            for hat_name, hat_json in category_hats.items():
                hat = Hat.from_json(hat_name, category_name, self, hat_json)

                if hat.custom_model_data in self.cmd_to_hat_map:
                    raise Exception(
                        f"Can't add {hat}, Custom Model Data {self.cmd_to_hat_map[hat.custom_model_data]} already has the same Custom Model Data"
                    )

                self.cmd_to_hat_map[hat.custom_model_data] = hat
                hats.append(hat)

            self.categories[category_name] = hats

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
    def from_json(cls, name: str, category: str, registry: Registry, json: Dict):
        categorized_name = f"{category}{{0}}{name}"

        cmd = registry.custom_model_data_id * 10000 + json["cmd"]

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


################
# CLI Commands #
################


def cmd_max(argv):
    registry = Registry()
    max_cmd, max_hat = max(registry.cmd_to_hat_map.items(), key=lambda x: x[0])
    print(max_cmd, max_hat)


def cmd_min(argv):
    registry = Registry()
    min_cmd, min_hat = min(registry.cmd_to_hat_map.items(), key=lambda x: x[0])
    print(min_cmd, min_hat)


def cmd_list(argv):
    registry = Registry()
    for cmd, hat in sorted(registry.cmd_to_hat_map.items(), key=lambda x: x[0]):
        print(cmd, hat)


def cmd_free(argv):
    registry = Registry()
    custom_model_data = sorted(registry.cmd_to_hat_map.keys())
    min_cmd, _ = min(registry.cmd_to_hat_map.items(), key=lambda x: x[0])
    max_cmd, _ = max(registry.cmd_to_hat_map.items(), key=lambda x: x[0])

    for i in range(min_cmd, max_cmd):
        if i not in custom_model_data:
            print(i)


def cmd_custom_model_data(argv):
    CMD_MAX = "max"
    CMD_MIN = "min"
    CMD_LIST = "list"
    CMD_FREE = "free"
    SUB_COMMANDS = [CMD_MAX, CMD_MIN, CMD_LIST, CMD_FREE]

    parser = argparse.ArgumentParser(
        description="Custom Model Data commands",
        usage=f"%(prog)s {CMD_CUSTOM_MODEL_DATA} [-h] {{{SUB_COMMANDS}}}",
    )
    parser.add_argument("command", type=str, choices=SUB_COMMANDS, help="Subcommand to run")
    args = parser.parse_args(argv[0:1])

    if args.command == CMD_MAX:
        cmd_max(sys.argv[2:])
    elif args.command == CMD_MIN:
        cmd_min(sys.argv[2:])
    elif args.command == CMD_LIST:
        cmd_list(sys.argv[2:])
    elif args.command == CMD_FREE:
        cmd_free(sys.argv[2:])


########
# MAIN #
########

CMD_CUSTOM_MODEL_DATA = "cmd"
COMMANDS = [CMD_CUSTOM_MODEL_DATA]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Registry for hat items")
    parser.add_argument("command", type=str, choices=COMMANDS, help="Subcommand to run")
    args = parser.parse_args(sys.argv[1:2])

    if args.command == CMD_CUSTOM_MODEL_DATA:
        cmd_custom_model_data(sys.argv[2:])
