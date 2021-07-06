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
    ctx.assets.merge(item_models(ctx, opts.cmd_id))


def item_models(ctx: Context, cmd_id: int):
    """Create item models used for custom model data"""

    assets = ResourcePack()

    registry = HatRegistry.get(cmd_id)

    overrides = []
    for category, hats in registry.categories.items():
        overrides += [ModelOverride(hat.cmd, hat.model_path(category)) for hat in hats]
    overrides = sorted(overrides, key=lambda o: o.cmd)

    assets.models["minecraft:item/stick"] = Model(
        ctx.template.render("models/stick.json", overrides=overrides)
    )
    assets.models["minecraft:item/leather_helmet"] = Model(
        ctx.template.render("models/leather_helmet.json", overrides=overrides)
    )

    return assets
