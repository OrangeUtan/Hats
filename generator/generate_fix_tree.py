import os

from registry import Hat, Registry


def fix_tags_command(hat) -> str:
    return f'data modify storage minecraft:hats hat_to_fix.tag.Tags set value ["hats.hat", "{hat.type}"]'


def fix_name_command(hat) -> str:
    return f'data modify storage minecraft:hats hat_to_fix.tag.display.Name set value \'{{"translate":"{hat.translation}"}}\''


def fix_lore_command(hat) -> str:
    if hat.lore:
        lines = [f'{{"translate": "{line}"}}' for line in hat.lore]
        return (
            f"data modify storage minecraft:hats hat_to_fix.tag.display.Lore set value {lines}"
        )
    else:
        return ""


def write_lines(lines, file):
    for i in range(len(lines)):
        if i > 0:
            file.write("\n")
        file.write(lines[i])


def create_tree_file_for(root_dir, hat_old_cmd_pairs):
    min_cmd = hat_old_cmd_pairs[0][1]
    max_cmd = hat_old_cmd_pairs[-1][1]

    with open(f"{root_dir}/tree-{min_cmd}-{max_cmd}.mcfunction", "w+") as file:
        lines = []

        if len(hat_old_cmd_pairs) > 4:
            create_tree_file_for(
                root_dir, hat_old_cmd_pairs[: int(len(hat_old_cmd_pairs) / 2)]
            )
            create_tree_file_for(
                root_dir, hat_old_cmd_pairs[int(len(hat_old_cmd_pairs) / 2) :]
            )

            split_cmd = hat_old_cmd_pairs[: int(len(hat_old_cmd_pairs) / 2)][-1][1]
            lines += [
                f"execute if score @s hats.math matches {min_cmd}..{split_cmd} run function oran9eutan:hats/fix_old_hats/tree/tree-{min_cmd}-{split_cmd}"
            ]
            lines += [
                f"execute if score @s hats.math matches {split_cmd+1}..{max_cmd} run function oran9eutan:hats/fix_old_hats/tree/tree-{split_cmd+1}-{max_cmd}"
            ]
        else:
            lines = []
            for hat, old_cmd in hat_old_cmd_pairs:
                lines += [
                    f"execute if score @s hats.math matches {old_cmd} run function oran9eutan:hats/fix_old_hats/tree/{hat.type}"
                ]

        write_lines(lines, file)


registry = Registry.from_json()
tree_root_dir = f"{registry.functions_dir}/fix_old_hats/tree"

if not os.path.exists(tree_root_dir):
    os.makedirs(tree_root_dir)

# Create a dictionary of old custom model data. Initialise with cmd that didn't change
hat_type_to_old_cmd_map = {
    "hats.hat.type.fez": 3000,
    "hats.hat.type.squid": 3001,
    "hats.hat.type.arrow_prop": 3002,
    "hats.hat.type.frying_pan": 3003,
    "hats.hat.type.3D_glasses": 3145,
    "hats.hat.type.dog": 7773190,
    "hats.hat.type.earth_in_orbit": 7773191,
    "hats.hat.type.wiggly_ghast": 7773180,
    "hats.hat.type.native_american_headband": 7773181,
    "hats.hat.type.jason_mask": 7773182,
}
# Add remaining hats for which the CMD ID was added to their cmd
for _, hat in registry.cmd_to_hat_map.items():
    if not hat.type in hat_type_to_old_cmd_map:
        hat_type_to_old_cmd_map[hat.type] = hat.custom_model_data - 7770000


# Create files for individual hats
for _, hat in registry.cmd_to_hat_map.items():
    # Generate lines
    lines = [fix_tags_command(hat), fix_name_command(hat)]
    if hat.lore:
        lines.append(fix_lore_command(hat))

    with open(f"{tree_root_dir}/{hat.type}.mcfunction", "w+") as file:
        write_lines(lines, file)

# Create tree files
hat_old_cmd_pairs = list(
    map(lambda x: (x[1], hat_type_to_old_cmd_map[x[1].type]), registry.cmd_to_hat_map.items())
)
create_tree_file_for(tree_root_dir, sorted(hat_old_cmd_pairs, key=lambda x: x[1]))
