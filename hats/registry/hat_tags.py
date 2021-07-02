from pathlib import Path

import yaml

from hats.registry.hats import HatRegistry


class HatTagRegistry(dict):
    PATH = Path("hats/registry/hat_tags.yml")

    @classmethod
    def get(cls) -> dict[str, list[str]]:
        with cls.PATH.open("r") as f:
            return yaml.safe_load(f)
