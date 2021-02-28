from generator.registry import Item
from registry import Hat, Registry
from pathlib import Path
from dataclasses import dataclass


@dataclass
class LootTable:
    rel_path: Path
    json: dict
    format_json: bool


def create_hat_loot_table(hat: Hat, item: Item, rel_path: Path):
    functions = [
        {"function": "minecraft:set_name", "name": {"translate": hat.translation}},
        {
            "function": "set_nbt",
            "tag": f'{{CustomModelData:{hat.custom_model_data}, Tags:["hats.hat", "{hat.type}"]}}',
        },
    ]

    # Add lore lines if any exist
    if hat.lore:
        lines = [{"translate": f"{line}"} for line in hat.lore]
        functions.append({"function": "minecraft:set_lore", "lore": lines})

    json = {
        "type": "minecraft:generic",
        "pools": [
            {
                "functions": functions,
                "rolls": 1,
                "entries": [{"type": "minecraft:item", "name": item.id}],
            }
        ],
    }

    return LootTable(rel_path, json, True)


def create_all_hats_from_category_loot_table(
    category_hats: list[Hat], subfolder: str, rel_path: Path
):
    pools = []
    for hat in category_hats:
        pools.append(
            {
                "rolls": 1,
                "entries": [
                    {
                        "type": "minecraft:loot_table",
                        "name": f"oran9eutan:hats/{subfolder}/{hat.category}/{hat.name}",
                    }
                ],
            }
        )

    json = {"type": "minecraft:generic", "pools": pools}

    return LootTable(Path(subfolder, rel_path), json, False)


def create_random_hat_from_category_loot_table(
    category_hats: list[Hat], subfolder: str, rel_path: Path
):
    options = []
    for hat in category_hats:
        options.append(
            {
                "type": "minecraft:loot_table",
                "name": f"oran9eutan:hats/{subfolder}/{hat.category}/{hat.name}",
            }
        )

    json = {
        "type": "minecraft:generic",
        "pools": [{"rolls": 1, "entries": options}],
    }

    return LootTable(Path(subfolder, rel_path), json, False)


def create_hat_loot_tables(registry: Registry):
    loot_tables: list[LootTable] = []

    for _, hat in registry.cmd_to_hat_map.items():
        item_inv = registry.get_item_inv(hat.item_inv)
        item_on_head = registry.get_item_on_head(hat.item_on_head)

        loot_tables.append(
            create_hat_loot_table(hat, item_inv, Path("hat", hat.category, hat.name + ".json"))
        )
        loot_tables.append(
            create_hat_loot_table(
                hat, item_on_head, Path("hat_on_head", hat.category, hat.name + ".json")
            )
        )

    return loot_tables


def create_special_hat_loot_tables(registry: Registry):
    loot_tables: list[LootTable] = []
    for category_name, category_hats in registry.categories.items():
        loot_tables.append(
            create_all_hats_from_category_loot_table(
                category_hats, "hat", Path(category_name, "_all.json")
            )
        )
        loot_tables.append(
            create_random_hat_from_category_loot_table(
                category_hats, "hat", Path(category_name, "_rand.json")
            )
        )

    # Generate additional loot tables used by the datapack
    loot_tables.append(
        create_random_hat_from_category_loot_table(
            registry.categories["cats"], "hat_on_head", Path("cats", "_rand.json")
        )
    )
    loot_tables.append(
        create_random_hat_from_category_loot_table(
            registry.categories["villager"], "hat_on_head", Path("villager", "_rand.json")
        )
    )

    return loot_tables
