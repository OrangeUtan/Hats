from pathlib import Path

from invoke import task

RESOURCEPACK_DIR = Path("resourcepack")
DATAPACK_DIR = Path("datapack")


@task
def setup(c):
    c.run("poetry lock -n")
    c.run("poetry install -n")
    c.run("poetry run pre-commit install")


@task
def format(c):
    c.run("poetry run black . --config pyproject.toml")
    c.run("poetry run isort . --settings-path pyproject.toml")


@task
def gen_loot_tables(c):
    c.run(f"poetry run py generator/cli.py generate hat-loot-tables .")


@task
def gen_localization(c, verbose=False):
    c.run(
        f'poetry run babelbox resourcepack/assets/minecraft/lang -pn --indent "\t" {"-v" if verbose else ""}'
    )


@task
def bump(c, version, dry=False):
    flags = "--dry-run" if dry else ""
    c.run(f"poetry run tbump {version} {flags}")


@task
def release(c):
    c.run(f"poetry run beet --config beet-release.json")
