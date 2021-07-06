from logging import getLogger

from beet import Context, DataPack, LootTable

from hats.registry.hats import Hat, HatRegistry

logger = getLogger(__name__)


def beet_default(ctx: Context):
    namespace = ctx.meta["namespace"]
    config = ctx.meta["hats"]
    cmd_id = int(config["cmd_id"])

    ctx.data.merge(_create_loot_tables(ctx, namespace, cmd_id))


def _create_loot_tables(ctx: Context, namespace: str, cmd_id: int):
    data = DataPack()

    registry = HatRegistry.get(cmd_id)

    for category, hats in registry.categories.items():
        # Create category loot tables
        for model_type in ["hat", "hat_on_head"]:
            data.loot_tables[
                f"{namespace}/{model_type}/{category}/all"
            ] = _create_all_hats_from_collection_loot_table(ctx, hats, namespace, model_type)
            data.loot_tables[
                f"{namespace}/{model_type}/{category}/random"
            ] = _create_random_hat_from_collection_loot_table(ctx, hats, namespace, model_type)

        # Create hat loot tables
        for hat in hats:
            data.loot_tables[f"{namespace}/hat_on_head/{hat.type}"] = _create_hat_loot_table(
                ctx, hat, hat.model_head
            )
            data.loot_tables[f"{namespace}/hat/{hat.type}"] = _create_hat_loot_table(
                ctx, hat, hat.model_inventory
            )

    return data


def _create_hat_loot_table(ctx: Context, hat: Hat, item_model_id: str):
    return LootTable(
        ctx.template.render(
            "loot_tables/hat.json",
            nbt_tag={"CustomModelData": hat.cmd, "Tags": ["hats.hat", hat.type_tag]},
            localized_name=hat.localized_name,
            item_model_id=item_model_id,
            localized_lore=hat.localized_lore,
        )
    )


def _create_all_hats_from_collection_loot_table(
    ctx: Context, hats: list[Hat], namespace: str, model_type: str
):
    return LootTable(
        ctx.template.render(
            "loot_tables/all_from_collection.json",
            loot_tables=[f"{namespace}/{model_type}/{hat.type}" for hat in hats],
        )
    )


def _create_random_hat_from_collection_loot_table(
    ctx: Context, hats: list[Hat], namespace: str, model_type: str
):
    return LootTable(
        ctx.template.render(
            "loot_tables/random_from_collection.json",
            loot_tables=[f"{namespace}/{model_type}/{hat.type}" for hat in hats],
        )
    )
