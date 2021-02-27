import os, json
from registry import Registry, Hat


def generate_loot_table_all_for_category(registry, category_name, category_hats, subfolder):
    pools = []
    for hat in category_hats:
        if hat.category == "*":
            rel_path = f"{hat.name}"
        else:
            rel_path = f"{hat.category}/{hat.name}"

        hat_pool = {
            "rolls": 1,
            "entries": [
                {
                    "type": "minecraft:loot_table",
                    "name": f"oran9eutan:hats/{subfolder}/{rel_path}",
                }
            ],
        }
        pools.append(hat_pool)

    loot_table_all = {"type": "minecraft:generic", "pools": pools}

    loot_table_all_path = f"{registry.loot_tables_dir}/{subfolder}/{category_name}/_all.json"
    parent_dir = os.path.split(loot_table_all_path)[0]
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)

    with open(loot_table_all_path, "w+") as file:
        json.dump(loot_table_all, file)


def generate_loot_table_rand_for_category(registry, category_name, category_hats, subfolder):
    entries = []
    for hat in category_hats:
        if hat.category == "*":
            rel_path = f"{hat.name}"
        else:
            rel_path = f"{hat.category}/{hat.name}"

        hat_entry = {
            "type": "minecraft:loot_table",
            "name": f"oran9eutan:hats/{subfolder}/{rel_path}",
        }

        entries.append(hat_entry)

    loot_table_rand = {
        "type": "minecraft:generic",
        "pools": [{"rolls": 1, "entries": entries}],
    }

    loot_table_rand_path = f"{registry.loot_tables_dir}/{subfolder}/{category_name}/_rand.json"
    parent_dir = os.path.split(loot_table_rand_path)[0]
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)

    with open(loot_table_rand_path, "w+") as file:
        json.dump(loot_table_rand, file)


registry = Registry.from_json()

for category_name, category_hats in registry.categories.items():
    generate_loot_table_all_for_category(registry, category_name, category_hats, "hat")
    generate_loot_table_rand_for_category(registry, category_name, category_hats, "hat")

    if category_name == "cats" or category_name == "villager":
        generate_loot_table_rand_for_category(
            registry, category_name, category_hats, "hat_on_head"
        )
