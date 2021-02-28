import json
from pathlib import Path
import typer
import itertools

from generator.registry import Registry
from generator import utils
from generator import loot_tables

app = typer.Typer()
cmd_app = typer.Typer()
app.add_typer(cmd_app, name="cmd")


@app.command()
def gen_loot_tables():
    registry = Registry.from_json()
    hat_loot_tables = loot_tables.create_hat_loot_tables(registry)
    category_loot_tables = loot_tables.create_special_hat_loot_tables(registry)

    for loot_table in itertools.chain(hat_loot_tables, category_loot_tables):
        path = Path(registry.loot_tables_dir, loot_table.rel_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        with path.open("w+") as f:
            if loot_table.format_json:
                json.dump(loot_table.json, f, separators=(",", ":"), indent=4)
            else:
                json.dump(loot_table.json, f)


@cmd_app.command()
def ls():
    registry = Registry.from_json()
    for cmd, hat in sorted(registry.cmd_to_hat_map.items(), key=lambda x: x[0]):
        print(cmd, f"{hat.category}.{hat.name}")


@cmd_app.command()
def stats():
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
