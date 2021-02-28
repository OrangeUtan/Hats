from pathlib import Path
from registry import Hat, Registry


class AllFromCategoryLootTable:
    def __init__(self, category_hats: list[Hat], subfolder: str, rel_path: Path):
        self.rel_path = Path(subfolder, rel_path)

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

        self.json = {"type": "minecraft:generic", "pools": pools}


class RandFromCategoryLootTable:
    def __init__(self, category_hats: list[Hat], subfolder: str, rel_path: Path):
        self.rel_path = Path(subfolder, rel_path)

        options = []
        for hat in category_hats:
            options.append(
                {
                    "type": "minecraft:loot_table",
                    "name": f"oran9eutan:hats/{subfolder}/{hat.category}/{hat.name}",
                }
            )

        self.json = {
            "type": "minecraft:generic",
            "pools": [{"rolls": 1, "entries": options}],
        }


def create_special_hat_loot_tables(registry: Registry):
    loot_tables = []
    for category_name, category_hats in registry.categories.items():
        loot_tables.append(
            AllFromCategoryLootTable(category_hats, "hat", Path(category_name, "_all.json"))
        )
        loot_tables.append(
            RandFromCategoryLootTable(category_hats, "hat", Path(category_name, "_rand.json"))
        )

    # Generate additional loot tables used by the datapack
    loot_tables.append(
        RandFromCategoryLootTable(
            registry.categories["cats"], "hat_on_head", Path("cats", "_rand.json")
        )
    )
    loot_tables.append(
        RandFromCategoryLootTable(
            registry.categories["villager"], "hat_on_head", Path("villager", "_rand.json")
        )
    )

    return loot_tables
