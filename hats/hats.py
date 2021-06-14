from collections import defaultdict
from dataclasses import dataclass


@dataclass(init=False, unsafe_hash=True)
class Hat:
    name: str
    type: str
    cmd: int
    num_lore_lines: int

    model_head: str
    model_inventory: str

    DEFAULT_MODEL_HEAD = "stick"
    DEFAULT_MODEL_INVENTORY = "leather_helmet"

    def __init__(
        self,
        name: str,
        type: str,
        cmd: int,
        cmd_id: int,
        num_lore_lines: int = 0,
        model_head=DEFAULT_MODEL_HEAD,
        model_inventory=DEFAULT_MODEL_INVENTORY,
    ):
        self.name = name
        self.type = type
        self.cmd = cmd_id * 10000 + cmd
        self.num_lore_lines = num_lore_lines
        self.model_head = model_head
        self.model_inventory = model_inventory

    @classmethod
    def from_json(cls, name: str, cmd_id: int, json: dict):
        return Hat(
            name,
            json["type"],
            json["cmd"],
            cmd_id,
            json.get("num_lore_lines", 0),
            json.get("model_head", Hat.DEFAULT_MODEL_HEAD),
            json.get("model_inventory", Hat.DEFAULT_MODEL_INVENTORY),
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


class HatRegistry:
    DEFAULT_CATEGORY = "misc"

    def __init__(self):
        self.name_to_hat_map: dict[str, Hat] = {}
        self.cmd_to_hat_map: dict[int, Hat] = {}
        self.name_to_category_map: dict[str, str] = {}
        self.categories: defaultdict[str, list[Hat]] = defaultdict(list)

    @classmethod
    def from_json(cls, cmd_id: int, json: dict):
        registry = HatRegistry()

        for category, hats_json in json.items():
            for hat_name, hat_json in hats_json.items():
                registry.add(Hat.from_json(hat_name, cmd_id, hat_json), category)

        return registry

    def add(self, hat: Hat, category=DEFAULT_CATEGORY):
        self.name_to_hat_map[hat.name] = hat
        self.cmd_to_hat_map[hat.cmd] = hat
        self.name_to_category_map[hat.name] = category
        self.categories[category].append(hat)

    def by_name(self, name: str):
        return self.name_to_hat_map[name]

    def by_cmd(self, cmd: int):
        return self.cmd_to_hat_map[cmd]

    def category_of(self, hat_name: str):
        return self.name_to_category_map[hat_name]
