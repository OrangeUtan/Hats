from dataclasses import dataclass
from logging import getLogger

from beet import Context, Model, ResourcePack

from hats.options import HatsOptions
from hats.registry.hats import HatRegistry

logger = getLogger(__name__)


@dataclass
class ModelOverride:
    cmd: int
    model: str


def beet_default(ctx: Context):
    opts = HatsOptions.from_json(ctx.meta["hats"])
    ctx.assets.merge(item_models(ctx, opts))


def item_models(ctx: Context, opts: HatsOptions):
    """Create item models used for custom model data"""

    assets = ResourcePack()

    registry = HatRegistry.get(opts.cmd_id)

    overrides = []
    for category, hats in registry.categories.items():
        overrides += [ModelOverride(hat.cmd, hat.model_path(category)) for hat in hats]
    overrides = sorted(overrides, key=lambda o: o.cmd)

    item_head_name = opts.default_item_head.split(":")[1]
    item_inventory_name = opts.default_item_inventory.split(":")[1]

    assets.models[f"minecraft:item/{item_head_name}"] = Model(
        ctx.template.render(f"models/{item_head_name}.json", overrides=overrides)
    )
    assets.models[f"minecraft:item/{item_inventory_name}"] = Model(
        ctx.template.render(f"models/{item_inventory_name}.json", overrides=overrides)
    )

    return assets
