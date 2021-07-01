from logging import getLogger
from pathlib import Path

import yaml
from beet import Context

from hats.hats import HatRegistry

logger = getLogger(__name__)


def beet_default(ctx: Context):
    namespace = ctx.meta["namespace"]
    config = ctx.meta["hats"]
    registry_path = Path(config["registry"])
    cmd_id = int(config["cmd_id"])

    with registry_path.open("r") as f:
        registry = HatRegistry.from_json(cmd_id, yaml.safe_load(f))

    type_to_hat_meta_map = {}
    categories = {}
    for category, hats in registry.categories.items():
        category_hat_metas = []
        for hat in hats:
            hat_meta = {"cmd": hat.cmd, "type_tag": hat.type_tag, "type": hat.type}
            type_to_hat_meta_map[hat.type] = hat_meta
            category_hat_metas.append(hat_meta)
        categories[category] = category_hat_metas

    config["all"] = list(type_to_hat_meta_map.values())
    config["hat"] = type_to_hat_meta_map
    config["category"] = categories
