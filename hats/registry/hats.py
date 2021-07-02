from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass(init=False, unsafe_hash=True)
class Hat:
    type: str
    cmd: int
    num_lore_lines: int

    model_head: str
    model_inventory: str

    DEFAULT_MODEL_HEAD = "stick"
    DEFAULT_MODEL_INVENTORY = "leather_helmet"

    def __init__(
        self,
        type: str,
        cmd: int,
        cmd_id: int,
        num_lore_lines: int = 0,
        model_head=DEFAULT_MODEL_HEAD,
        model_inventory=DEFAULT_MODEL_INVENTORY,
        model=None,
    ):
        self.type = type
        self.cmd = cmd_id * 10000 + cmd
        self.num_lore_lines = num_lore_lines
        self.model_head = model_head
        self.model_inventory = model_inventory
        self._model = model

    @classmethod
    def from_json(cls, type: str, cmd_id: int, json: dict):
        return Hat(
            type,
            json["cmd"],
            cmd_id,
            json.get("num_lore_lines", 0),
            json.get("model_head", Hat.DEFAULT_MODEL_HEAD),
            json.get("model_inventory", Hat.DEFAULT_MODEL_INVENTORY),
            json.get("model", None),
        )

    @property
    def localized_name(self):
        return f"item.hats.hat.{self.type}.name"

    @property
    def localized_lore(self):
        return [f"item.hats.hat.{self.type}.lore{i+1}" for i in range(self.num_lore_lines)]

    @property
    def type_tag(self):
        return f"hats.hat.type.{self.type}"

    def model_path(self, category: str):
        return f"item/hats/{category}/{self.type}"


class HatRegistry:
    PATH = Path("hats/registry/hats.yml")

    def __init__(self):
        self.cmd_to_hat_map: dict[int, Hat] = {}
        self.type_to_category_map: dict[str, str] = {}
        self.type_to_hat_map: dict[str, Hat] = {}
        self.categories: defaultdict[str, list[Hat]] = defaultdict(list)

    @classmethod
    def from_json(cls, cmd_id: int, json: dict):
        registry = HatRegistry()

        for category, hats_json in json.items():
            for hat_type, hat_json in hats_json.items():
                registry.add(Hat.from_json(hat_type, cmd_id, hat_json), category)

        return registry

    @classmethod
    def get(cls, cmd_id: int):
        with cls.PATH.open("r") as f:
            return cls.from_json(cmd_id, yaml.safe_load(f))

    @property
    def hats(self):
        return self.type_to_hat_map.values()

    def add(self, hat: Hat, category: str):
        self.type_to_hat_map[hat.type] = hat
        self.cmd_to_hat_map[hat.cmd] = hat
        self.type_to_category_map[hat.type] = category
        self.type_to_hat_map[hat.type] = hat
        self.categories[category].append(hat)

    def by_type(self, type: str):
        return self.type_to_hat_map[type]

    def by_cmd(self, cmd: int):
        return self.cmd_to_hat_map[cmd]

    def category_of(self, type: str):
        return self.type_to_category_map[type]
