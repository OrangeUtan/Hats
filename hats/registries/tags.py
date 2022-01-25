from collections import defaultdict
from pathlib import Path

import yaml

from hats.registries.hats import Hat


class TagRegistry:
    PATH = Path("src/tags.yml")

    def __init__(self):
        self.tag_to_types: dict[str, set[Hat]] = defaultdict(set)
        self.type_to_tags: dict[str, set[str]] = defaultdict(set)

    @classmethod
    def from_json(cls, json: dict):
        registry = TagRegistry()

        for tag, hat_types in json.items():
            for hat_type in hat_types:
                if hat_type[0] == "#":
                    for hat_type in registry.tag_to_types[hat_type[1:]]:
                        registry.add(tag, hat_type)
                else:
                    registry.add(tag, hat_type)

        return registry

    @classmethod
    def get(cls):
        with cls.PATH.open("r") as f:
            return cls.from_json(yaml.safe_load(f))

    def add(self, tag: str, hat_type: str):
        self.tag_to_types[tag].add(hat_type)
        self.type_to_tags[hat_type].add(tag)
