from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass
class ShapelessHatRecipe:
    hat_type: str
    ingredients: dict


class HatRecipeRegistry:
    PATH = Path("hats/registry/hat_recipes.yml")

    def __init__(self, recipes: dict[str, list[ShapelessHatRecipe]]):
        self.recipes = recipes

    @classmethod
    def from_json(cls, json: dict):
        hat_recipes: dict[str, list[ShapelessHatRecipe]] = defaultdict(list)
        for hat_type, recipes in json.items():
            for recipe in recipes:
                if recipe["type"] == "shapeless":
                    hat_recipes[hat_type].append(
                        ShapelessHatRecipe(hat_type, recipe["ingredients"])
                    )

        return HatRecipeRegistry(hat_recipes)

    @classmethod
    def get(cls):
        with cls.PATH.open("r") as f:
            return cls.from_json(yaml.safe_load(f))
