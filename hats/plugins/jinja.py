from logging import getLogger
from pathlib import Path

import yaml
from beet import Context

from hats.registry.hats import HatRegistry

logger = getLogger(__name__)

TAGS_PATH = Path("hats/registry/tags.yml")


def beet_default(ctx: Context):
    config = ctx.meta["hats"]
    cmd_id = int(config["cmd_id"])

    registry = HatRegistry.get(cmd_id)

    type_to_hat_meta_map = {}
    categories = {}
    for category, hat_types in registry.categories.items():
        category_hat_metas = []
        for hat in hat_types:
            hat_meta = {"cmd": hat.cmd, "type_tag": hat.type_tag, "type": hat.type}
            type_to_hat_meta_map[hat.type] = hat_meta
            category_hat_metas.append(hat_meta)
        categories[category] = category_hat_metas

    tags = {}
    with TAGS_PATH.open("r") as f:
        for tag, hat_types in yaml.safe_load(f).items():
            tags[tag] = [type_to_hat_meta_map[type] for type in hat_types]

    config["all"] = list(type_to_hat_meta_map.values())
    config["hat"] = type_to_hat_meta_map
    config["category"] = categories
    config["tag"] = tags
