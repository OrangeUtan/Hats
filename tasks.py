import shutil
from pathlib import Path

from invoke import task

BUILD_DIR = Path("build")


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
def clean_loot_tables(c):
    paths = [
        Path("datapack/data/oran9eutan/loot_tables/hats/hat"),
        Path("datapack/data/oran9eutan/loot_tables/hats/hat_on_head"),
    ]

    for path in paths:
        if path.exists():
            shutil.rmtree(path)


@task
def gen_loot_tables(c):
    clean_loot_tables(c)
    c.run("poetry run py generator/generate_hat_loot_tables.py")
    c.run("poetry run py generator/generate_special_hat_loot_tables.py")


@task
def clean(c):
    shutil.rmtree(BUILD_DIR)


@task
def build(c):
    c.run(f"poetry run py generator/cli.py build datapack {str(BUILD_DIR)}")
    c.run(f"poetry run py generator/cli.py build resourcepack {str(BUILD_DIR)}")
