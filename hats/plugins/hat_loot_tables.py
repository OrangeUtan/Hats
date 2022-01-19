from logging import getLogger

from beet import Context, DataPack, LootTable

from hats.options import HatsOptions
from hats.registries.hats import Hat, HatRegistry

logger = getLogger(__name__)


def beet_default(ctx: Context):
    namespace = ctx.meta["namespace"]
    opts = HatsOptions.from_json(ctx.meta["hats"])

    ctx.data.merge(_create_loot_tables(ctx, namespace, opts))


def _create_loot_tables(ctx: Context, namespace: str, opts: HatsOptions):
    data = DataPack()

    registry = HatRegistry.get(opts.cmd_id)

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
                ctx, hat, hat.item_head or opts.default_item_head
            )
            data.loot_tables[f"{namespace}/hat/{hat.type}"] = _create_hat_loot_table(
                ctx, hat, hat.item_inventory or opts.default_item_inventory
            )

    return data


def _create_hat_loot_table(ctx: Context, hat: Hat, item_model_id: str):
    nbt = {"CustomModelData": hat.cmd, "Tags": ["hats.hat", hat.type_tag]}
    if hat.additional_nbt:
        nbt.update(hat.additional_nbt)

    return LootTable(
        ctx.template.render(
            "loot_tables/hat.json",
            nbt_tag=nbt,
            localized_name=hat.localized_name,
            item_model_id=item_model_id,
            localized_lore=hat.lore,
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
