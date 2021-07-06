import textwrap
from logging import getLogger

from beet import Advancement, Context, DataPack, Function, Recipe

from hats.registry.hat_recipes import HatRecipeRegistry, ShapelessHatRecipe

logger = getLogger(__name__)


def beet_default(ctx: Context):
    namespace = ctx.meta["namespace"]
    hat_recipe_registry = HatRecipeRegistry.get()

    for hat_type, recipes in hat_recipe_registry.recipes.items():
        ctx.data.merge(_generate_recipes_for_hat(namespace, hat_type, recipes))
        ctx.data.merge(_generate_advancement_for_hat(namespace, hat_type, recipes))
        ctx.data.merge(_generate_function_for_hat(namespace, hat_type))


def _generate_recipes_for_hat(namespace: str, hat_type: str, recipes: list[ShapelessHatRecipe]):
    data = DataPack()

    for i, recipe in enumerate(recipes, start=1):
        if isinstance(recipe, ShapelessHatRecipe):
            suffix = f"_{i}" if len(recipes) > 1 else ""
            data.recipes[f"{namespace}/{hat_type}{suffix}"] = Recipe(
                {
                    "type": "minecraft:crafting_shapeless",
                    "ingredients": recipe.ingredients,
                    "result": {"item": "minecraft:knowledge_book", "count": 1},
                }
            )

    return data


def _generate_advancement_for_hat(namespace: str, hat_type: str, recipes: list[ShapelessHatRecipe]):
    data = DataPack()

    criteria = {}
    for i, recipe in enumerate(recipes, start=1):
        suffix = f"_{i}" if len(recipes) > 1 else ""
        criteria[f"recipe{suffix}"] = {
            "trigger": "minecraft:recipe_unlocked",
            "conditions": {"recipe": f"{namespace}/{hat_type}{suffix}"},
        }

    data.advancements[f"{namespace}/event/recipe/{hat_type}"] = Advancement(
        {
            "criteria": criteria,
            "requirements": [[c for c in criteria.keys()]],
            "rewards": {"function": f"{namespace}/event/recipe/{hat_type}"},
        }
    )

    return data


def _generate_function_for_hat(namespace: str, hat_type: str):
    data = DataPack()

    data.functions[f"{namespace}/event/recipe/{hat_type}"] = Function(
        textwrap.dedent(
            f"""
        loot give @s loot oran9eutan:hats/hat/{hat_type}
        clear @s knowledge_book 1

        # Reset
        advancement revoke @s only oran9eutan:hats/event/recipe/{hat_type}
        recipe take @s oran9eutan:hats/{hat_type}
    """
        )[1:]
    )

    return data
