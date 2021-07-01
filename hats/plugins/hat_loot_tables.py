import json
from logging import getLogger

import jinja2
from beet import Context, LootTable
from beet.library.data_pack import DataPack

from hats.registry.hats import Hat, HatRegistry

logger = getLogger(__name__)


def beet_default(ctx: Context):
    namespace = ctx.meta["namespace"]
    config = ctx.meta["hats"]
    cmd_id = int(config["cmd_id"])

    cache = ctx.cache["hats"]
    if cache.has_changed(HatRegistry.PATH, "hats/plugins/hat_loot_tables.py"):
        logger.info(f"Generating hat loot tables")
        data = _create_loot_tables(namespace, cmd_id)
        data.save(path=cache.get_path("loot_tables"), overwrite=True)
    else:
        logger.info("Using cached hat loot tables")
        data = DataPack(path=cache.get_path("loot_tables"))

    ctx.data.merge(data)


def _create_loot_tables(namespace: str, cmd_id: int):
    data = DataPack()

    registry = HatRegistry.get(cmd_id)

    env = jinja2.Environment(loader=jinja2.FileSystemLoader("hats/templates"))

    for category, hats in registry.categories.items():
        # Create category loot tables
        for model_type in ["hat", "hat_on_head"]:
            data.loot_tables[
                f"{namespace}/{model_type}/{category}/all"
            ] = _create_all_hats_from_collection_loot_table(env, hats, namespace, model_type)
            data.loot_tables[
                f"{namespace}/{model_type}/{category}/random"
            ] = _create_random_hat_from_collection_loot_table(env, hats, namespace, model_type)

        # Create hat loot tables
        for hat in hats:
            data.loot_tables[f"{namespace}/hat_on_head/{hat.type}"] = _create_hat_loot_table(
                env, hat, hat.model_head
            )
            data.loot_tables[f"{namespace}/hat/{hat.type}"] = _create_hat_loot_table(
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
    env: jinja2.Environment, hats: list[Hat], namespace: str, model_type: str
):
    template = env.get_template("loot_tables/all_from_collection.json")
    rendered = template.render(loot_tables=[f"{namespace}/{model_type}/{hat.type}" for hat in hats])
    return LootTable(json.loads(rendered))


def _create_random_hat_from_collection_loot_table(
    env: jinja2.Environment, hats: list[Hat], namespace: str, model_type: str
):
    template = env.get_template("loot_tables/random_from_collection.json")
    rendered = template.render(loot_tables=[f"{namespace}/{model_type}/{hat.type}" for hat in hats])
    return LootTable(json.loads(rendered))
