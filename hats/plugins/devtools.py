from logging import getLogger

from beet import Context
from beet.library.data_pack import DataPack, Function

from hats.registry.hats import HatRegistry

logger = getLogger(__name__)


def beet_default(ctx: Context):
    namespace = ctx.meta["namespace"]
    config = ctx.meta["hats"]
    cmd_id = int(config["cmd_id"])

    registry = HatRegistry.get(cmd_id)

    ctx.data.merge(_generate_category_fashion_show_functions(namespace, registry))


def _generate_category_fashion_show_functions(namespace: str, registry: HatRegistry):
    data = DataPack()

    for category, hats in registry.categories.items():
        lines = []
        for i, hat in enumerate(hats):
            lines += [
                f"execute if score #show_progress hats.math matches {i} run loot replace entity @e[tag=fashion_model] armor.head loot {namespace}/hat_on_head/{hat.type}",
                f'execute if score #show_progress hats.math matches {i} run title @a subtitle {{"translate": "item.hats.hat.{hat.type}.name"}}',
            ]

        lines += [
            f'title @a title {{"text": ""}}',
            "scoreboard players add #show_progress hats.math 1",
            f"execute if score #show_progress hats.math matches {len(hats)}.. run scoreboard players set #show_progress hats.math 0",
        ]

        data.functions[f"{namespace}/dev/fashion_show_{category}"] = Function("\n".join(lines))

    return data
