from collections import defaultdict
from pathlib import Path

import yaml

from hats.registry.hats import HatRegistry


class HatTagRegistry(dict):
    PATH = Path("src/tags.yml")

    @classmethod
    def from_json(cls, json: dict):
        registry: dict[str, list[str]] = defaultdict(list)
        for tag, hat_types in json.items():
            for hat_type in hat_types:
                if hat_type[0] == "#":
                    registry[tag] += registry[hat_type[1:]]
                else:
                    registry[tag].append(hat_type)
        return registry

    @classmethod
    def get(cls):
        with cls.PATH.open("r") as f:
            return cls.from_json(yaml.safe_load(f))
