from generator.registry import Item
from registry import Hat, Registry
from pathlib import Path


class HatLootTable:
    def __init__(self, hat: Hat, item: Item, rel_path: Path):
        self.rel_path = rel_path

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

        self.json = {
            "type": "minecraft:generic",
            "pools": [
                {
                    "functions": functions,
                    "rolls": 1,
                    "entries": [{"type": "minecraft:item", "name": item.id}],
                }
            ],
        }


def create_hat_loot_tables(registry: Registry):
    loot_tables = []

    for _, hat in registry.cmd_to_hat_map.items():
        item_inv = registry.get_item_inv(hat.item_inv)
        item_on_head = registry.get_item_on_head(hat.item_on_head)

        loot_tables.append(
            HatLootTable(hat, item_inv, Path("hat", hat.category, hat.name + ".json"))
        )
        loot_tables.append(
            HatLootTable(
                hat, item_on_head, Path("hat_on_head", hat.category, hat.name + ".json")
            )
        )

    return loot_tables
