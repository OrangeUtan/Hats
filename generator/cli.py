import json
from pathlib import Path
import typer
import itertools
import shutil
import os

from generator.registry import Registry
from generator import utils
from generator import loot_tables

app = typer.Typer()
cmd_app = typer.Typer(short_help="Perform Custom Model Data queries")
gen_app = typer.Typer(short_help="Generate files")
app.add_typer(cmd_app, name="cmd")
app.add_typer(gen_app, name="gen")


@app.command(name="build-datapack")
def cli_build_datapack():
    build_dir = Path("build")
    print(build_dir.absolute())

    for dir_name, _, files in os.walk(Path("datapack")):
        dst_dir = Path(build_dir, dir_name)
        dst_dir.mkdir(parents=True, exist_ok=True)

        for file in files:
            src_path = Path(dir_name, file)
            dst_path = Path(dst_dir, file)
            shutil.copy(src_path, dst_path)


@app.command(name="build-resourcepack")
def cli_build_resourcepack():
    build_dir = Path("build")
    print(build_dir.absolute())

    for dir_name, _, files in os.walk(Path("resourcepack")):
        dst_dir = Path(build_dir, dir_name)
        dst_dir.mkdir(parents=True, exist_ok=True)

        for file in files:
            src_path = Path(dir_name, file)
            dst_path = Path(dst_dir, file)
            shutil.copy(src_path, dst_path)


@gen_app.command(name="loot-tables", short_help="Generate all hat loot tables")
def cli_gen_loot_tables():
    registry = Registry.from_json()
    hat_loot_tables = loot_tables.create_hat_loot_tables(registry)
    category_loot_tables = loot_tables.create_special_hat_loot_tables(registry)

    print(f"Generating {len(hat_loot_tables)} hat loot tables")
    print(f"Generating {len(category_loot_tables)} category loot tables")

    for loot_table in itertools.chain(hat_loot_tables, category_loot_tables):
        path = Path(registry.loot_tables_dir, loot_table.rel_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        with path.open("w+") as f:
            if loot_table.format_json:
                json.dump(loot_table.json, f, separators=(",", ":"), indent=4)
            else:
                json.dump(loot_table.json, f)


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


app()
