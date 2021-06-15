import json
from dataclasses import dataclass
from logging import getLogger
from pathlib import Path

import jinja2
from beet import Context, LootTable
from beet.library.data_pack import DataPack
from beet.library.resource_pack import Model, ResourcePack
from ruamel import yaml

from hats.hats import HatRegistry

logger = getLogger(__name__)

CACHE_KEY = "item_models"


@dataclass
class ModelOverride:
    cmd: int
    model: str


def beet_default(ctx: Context):
    namespace = ctx.meta["namespace"]
    config = ctx.meta["hats"]
    registry_path = Path(config["registry"])
    cmd_id = int(config["cmd_id"])

    cache = ctx.cache["hats"]
    if cache.has_changed(registry_path, "hats/plugins/item_models.py"):
        logger.info(f"Generating item models")
        assets = _create_item_models(namespace, registry_path, cmd_id)
        assets.save(path=cache.get_path(CACHE_KEY), overwrite=True)
    else:
        logger.info("Using cached item models")
        assets = ResourcePack(path=cache.get_path(CACHE_KEY))

    ctx.assets.merge(assets)


def _create_item_models(namespace: str, registry_path: Path, cmd_id: int):
    assets = ResourcePack()

    with registry_path.open("r") as f:
        registry = HatRegistry.from_json(cmd_id, yaml.safe_load(f))

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
