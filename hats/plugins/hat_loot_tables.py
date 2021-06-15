import json
from logging import getLogger
from pathlib import Path

import jinja2
from beet import Context, LootTable
from beet.library.data_pack import DataPack
from ruamel import yaml

from hats.hats import Hat, HatRegistry

logger = getLogger(__name__)


def beet_default(ctx: Context):
    namespace = ctx.meta["namespace"]
    config = ctx.meta["hats"]
    registry_path = Path(config["registry"])
    cmd_id = int(config["cmd_id"])

    cache = ctx.cache["hats"]
    if cache.has_changed(registry_path, "hats/plugins/hat_loot_tables.py"):
        logger.info(f"Generating hat loot tables")
        data = _create_loot_tables(namespace, registry_path, cmd_id)
        data.save(path=cache.get_path("loot_tables"), overwrite=True)
    else:
        logger.info("Using cached hat loot tables")
        data = DataPack(path=cache.get_path("loot_tables"))

    ctx.data.merge(data)


def _create_loot_tables(namespace: str, registry_path: Path, cmd_id: int):
    data = DataPack()

    with registry_path.open("r") as f:
        registry = HatRegistry.from_json(cmd_id, yaml.safe_load(f))

    env = jinja2.Environment(loader=jinja2.FileSystemLoader("hats/templates"))

    for category, hats in registry.categories.items():
        data.loot_tables[
            f"{namespace}/hat/{category}/_all"
        ] = _create_all_hats_from_collection_loot_table(env, hats, registry, namespace)
        data.loot_tables[
            f"{namespace}/hat/{category}/_rand"
        ] = _create_random_hat_from_collection_loot_table(env, hats, registry, namespace)
        for hat in hats:
            data.loot_tables[
                f"{namespace}/hat_on_head/{category}/{hat.name}"
            ] = _create_hat_loot_table(env, hat, hat.model_head)
            data.loot_tables[f"{namespace}/hat/{category}/{hat.name}"] = _create_hat_loot_table(
                env, hat, hat.model_inventory
            )

    return data


def _create_hat_loot_table(env: jinja2.Environment, hat: Hat, item_model_id: str):
    template = env.get_template("loot_tables/hat.json")
    rendered = template.render(
        nbt_tag={"CustomModelData": hat.cmd, "Tags": ["hats.hat", hat.type_tag]},
        localized_name=hat.localized_name,
        item_model_id=item_model_id,
        localized_lore=hat.localized_lore,
    )
    return LootTable(json.loads(rendered))


def _create_all_hats_from_collection_loot_table(
    env: jinja2.Environment, hats: list[Hat], registry: HatRegistry, namespace: str
):
    template = env.get_template("loot_tables/all_from_collection.json")
    rendered = template.render(
        loot_tables=[f"{namespace}/hat/{registry.category_of(hat.name)}/{hat.name}" for hat in hats]
    )
    return LootTable(json.loads(rendered))


def _create_random_hat_from_collection_loot_table(
    env: jinja2.Environment, hats: list[Hat], registry: HatRegistry, namespace: str
):
    template = env.get_template("loot_tables/random_from_collection.json")
    rendered = template.render(
        loot_tables=[f"{namespace}/hat/{registry.category_of(hat.name)}/{hat.name}" for hat in hats]
    )
    return LootTable(json.loads(rendered))
