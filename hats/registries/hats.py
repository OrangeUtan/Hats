import dataclasses
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import yaml
from dataclasses_json import dataclass_json


@dataclass_json
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

    @property
    def localized_name(self):
        return f"item.hats.hat.{self.type}.name"

    @property
    def type_tag(self):
        return f"hats.hat.type.{self.type}"

    def model_path(self, category: str):
        return f"item/hats/{category}/{self.type}"


class HatRegistry:
    CMDS_PATH = Path("src/cmds.yml")
    HATS_PATH = Path("src/hats.yml")
    CATEGORIES_PATH = Path("src/categories.yml")

    def __init__(self):
        self.cmd_to_hat_map: dict[int, Hat] = {}
        self.type_to_category_map: dict[str, str] = {}
        self.type_to_hat_map: dict[str, Hat] = {}
        self.categories: defaultdict[str, list[Hat]] = defaultdict(list)

    @classmethod
    def from_json(
        cls,
        cmd_id: int,
        hats_json: dict[str, dict],
        cmd_to_type_map: dict[int, str],
        category_to_types_map: dict[str, list[str]],
    ):
        registry = HatRegistry()

        type_to_cmd = {cmd_to_type_map[cmd]: cmd for cmd in cmd_to_type_map}

        for category, hat_types in category_to_types_map.items():
            for hat_type in hat_types:
                hat_json = hats_json[hat_type] or {}

                registry.add(
                    Hat(
                        type=hat_type,
                        cmd=type_to_cmd[hat_type],
                        cmd_id=cmd_id,
                        lore=hat_json.get("lore", []),
                        model=hat_json.get("model"),
                        item_head=hat_json.get("item_head"),
                        item_inventory=hat_json.get("item_inventory"),
                        additional_nbt=hat_json.get("nbt"),
                    ),
                    category,
                )

        return registry

    @classmethod
    def get(cls, cmd_id: int):
        with cls.HATS_PATH.open("r") as hats, cls.CMDS_PATH.open(
            "r"
        ) as cmds, cls.CATEGORIES_PATH.open("r") as categories:
            return cls.from_json(
                cmd_id, yaml.safe_load(hats), yaml.safe_load(cmds), yaml.safe_load(categories)
            )

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
