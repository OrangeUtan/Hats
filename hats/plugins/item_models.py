import json
from dataclasses import dataclass
from logging import getLogger

import jinja2
from beet import Context
from beet.library.resource_pack import Model, ResourcePack

from hats.registry.hats import HatRegistry

logger = getLogger(__name__)

CACHE_KEY = "item_models"


@dataclass
class ModelOverride:
    cmd: int
    model: str


def beet_default(ctx: Context):
    config = ctx.meta["hats"]
    cmd_id = int(config["cmd_id"])

    cache = ctx.cache["hats"]
    if cache.has_changed(HatRegistry.PATH, "hats/plugins/item_models.py"):
        logger.info(f"Generating item models")
        assets = _create_item_models(cmd_id)
        assets.save(path=cache.get_path(CACHE_KEY), overwrite=True)
    else:
        logger.info("Using cached item models")
        assets = ResourcePack(path=cache.get_path(CACHE_KEY))

    ctx.assets.merge(assets)


def _create_item_models(cmd_id: int):
    assets = ResourcePack()

    registry = HatRegistry.get(cmd_id)

    env = jinja2.Environment(loader=jinja2.FileSystemLoader("hats/templates"))

    overrides = []
    for category, hats in registry.categories.items():
        overrides += [ModelOverride(hat.cmd, hat.model_path(category)) for hat in hats]
    overrides = sorted(overrides, key=lambda o: o.cmd)

    assets.models["minecraft:item/stick"] = Model(
        json.loads(env.get_template("models/stick.json").render(overrides=overrides))
    )
    assets.models["minecraft:item/leather_helmet"] = Model(
        json.loads(env.get_template("models/leather_helmet.json").render(overrides=overrides))
    )

    return assets
