import typer

from generator.registry import Registry
from generator.utils import get_gaps_in_series, series_as_ranges, range_to_str

app = typer.Typer()
cmd_app = typer.Typer()
gen_app = typer.Typer()

app.add_typer(cmd_app, name="cmd")
app.add_typer(gen_app, name="gen")


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

    cmd_gaps = list(get_gaps_in_series(min_cmd, max_cmd, registry.cmd_to_hat_map))

    print(f"{len(registry.cmd_to_hat_map)} hats")
    print(f"Min: {min_cmd} {min_hat.category}.{min_hat.name}")
    print(f"Max: {max_cmd} {max_hat.category}.{max_hat.name}")
    print(
        f"Gaps ({len(cmd_gaps)}):",
        ",".join(map(lambda r: range_to_str(r), (series_as_ranges(cmd_gaps)))),
    )


@gen_app.command()
def gen():
    pass


app()
