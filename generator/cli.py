import itertools
import json
import os
import shutil
from pathlib import Path
from typing import Iterator

import typer

from generator import localization, loot_tables, utils
from generator.registry import Registry

app = typer.Typer()
cmd_app = typer.Typer(short_help="Perform Custom Model Data queries")
generate_app = typer.Typer(short_help="Generate files")
build_app = typer.Typer()
app.add_typer(cmd_app, name="cmd")
app.add_typer(generate_app, name="generate")
app.add_typer(build_app, name="build")

############
# generate #
############


@generate_app.command(name="hat-loot-tables", short_help="Generate all hat loot tables")
def cli_generate_loot_tables(out_dir: str):
    out_dir = Path(out_dir)

    registry = Registry.from_json()
    hat_loot_tables = loot_tables.create_hat_loot_tables(registry)
    category_loot_tables = loot_tables.create_special_hat_loot_tables(registry)

    print(f"Generating {len(hat_loot_tables)} hat loot tables")
    print(f"Generating {len(category_loot_tables)} category loot tables")

    for loot_table in itertools.chain(hat_loot_tables, category_loot_tables):
        path = Path(out_dir, registry.loot_tables_dir, loot_table.rel_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        with path.open("w+", encoding="utf-8") as f:
            if loot_table.format_json:
                json.dump(loot_table.json, f, separators=(",", ":"), indent=4)
            else:
                json.dump(loot_table.json, f)


def generate_localization(csvfiles: Iterator[str], dir: Path, out_dir: Path):
    locales = localization.get_locales_from_csvfiles(*csvfiles)
    print(f"Generating locales {list(locales.keys())}")

    for locale, strings_json in locales.items():
        with Path(out_dir, dir, f"{locale}.json").open("w", encoding="utf-8") as f:
            json.dump(strings_json, f, separators=(",", ":"), indent=4, ensure_ascii=False)


@generate_app.command(name="localization", short_help="Generate language translations")
def cli_generate_localization(out_dir: str):
    out_dir = Path(out_dir)

    for dir, files in map(
        lambda x: (Path(x[0]), map(lambda f: Path(x[0], f), x[2])),
        os.walk(Path("resourcepack/assets/minecraft/lang")),
    ):
        Path(out_dir, dir).mkdir(parents=True, exist_ok=True)

        if dir == Path("resourcepack/assets/minecraft/lang"):
            csvfiles = filter(lambda f: f.name.endswith(".csv"), files)
            generate_localization(csvfiles, dir, out_dir)


#########
# build #
#########

# @build_app.command(name="datapack")
# def cli_build_datapack(build_dir: str):
#     build_dir = Path(build_dir)
#     dir = Path("datapack")
#     shutil.copytree(dir, Path(build_dir, dir), dirs_exist_ok=True)


# @build_app.command(name="resourcepack")
# def cli_build_resourcepack(build_dir: str):
#     build_dir = Path(build_dir)

#     for dir, files in map(
#         lambda x: (Path(x[0]), map(lambda f: Path(x[0], f), x[2])),
#         os.walk(Path("resourcepack")),
#     ):
#         Path(build_dir, dir).mkdir(parents=True, exist_ok=True)

#         if dir == Path("resourcepack/assets/minecraft/lang"):
#             csvfiles = filter(lambda f: f.name.endswith(".csv"), files)
#             generate_lang_files(csvfiles, dir, build_dir)
#         else:
#             for file in files:
#                 shutil.copy(file, Path(build_dir, file))

#######
# cmd #
#######


@cmd_app.command(name="ls")
def cli_cmd_ls():
    registry = Registry.from_json()
    for cmd, hat in sorted(registry.cmd_to_hat_map.items(), key=lambda x: x[0]):
        print(cmd, f"{hat.category}.{hat.name}")


@cmd_app.command(name="stats")
def cli_cmd_stats():
    registry = Registry.from_json()

    min_cmd, min_hat = min(registry.cmd_to_hat_map.items(), key=lambda x: x[0])
    max_cmd, max_hat = max(registry.cmd_to_hat_map.items(), key=lambda x: x[0])

    cmd_gaps = list(utils.get_gaps_in_series(min_cmd, max_cmd, registry.cmd_to_hat_map))

    print(f"{len(registry.cmd_to_hat_map)} hats")
    print(f"Min: {min_cmd} {min_hat.category}.{min_hat.name}")
    print(f"Max: {max_cmd} {max_hat.category}.{max_hat.name}")
    print(
        f"Gaps ({len(cmd_gaps)}):",
        ",".join(map(lambda r: utils.range_to_str(r), (utils.series_as_ranges(cmd_gaps)))),
    )


if __name__ == "__main__":
    app()
