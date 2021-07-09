from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import yaml


@dataclass(init=False, unsafe_hash=True)
class Hat:
    type: str
    cmd: int
    lore: list[str]

    additional_nbt: Optional[dict]
    item_head: Optional[str]
    item_inventory: Optional[str]

    def __init__(
        self,
        type: str,
        cmd: int,
        cmd_id: int,
        item_head,
        item_inventory,
        lore: list[str] = [],
        additional_nbt: Optional[dict] = None,
        model=None,
    ):
        self.type = type
        self.cmd = cmd_id * 10000 + cmd
        self.lore = lore
        self.item_head = item_head
        self.item_inventory = item_inventory
        self._model = model
        self.additional_nbt = additional_nbt

    @classmethod
    def from_json(cls, type: str, cmd_id: int, json: dict):
        return Hat(
            type=type,
            cmd=json["cmd"],
            cmd_id=cmd_id,
            lore=json.get("lore", []),
            model=json.get("model"),
            item_head=json.get("item_head"),
            item_inventory=json.get("item_inventory"),
            additional_nbt=json.get("nbt"),
        )

    @property
    def localized_name(self):
        return f"item.hats.hat.{self.type}.name"

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
