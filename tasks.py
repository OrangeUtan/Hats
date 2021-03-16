from pathlib import Path

from invoke import task

# BUILD_DIR = Path("build")
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


# @task
# def clean(c):
#     shutil.rmtree(BUILD_DIR)


# @task
# def build(c):
#     c.run(f"poetry run py generator/cli.py build datapack {str(BUILD_DIR)}")
#     c.run(f"poetry run py generator/cli.py build resourcepack {str(BUILD_DIR)}")


@task
def gen_loot_tables(c):
    c.run(f"poetry run py generator/cli.py generate hat-loot-tables .")


@task
def gen_localization(c):
    c.run('poetry run babelbox resourcepack/assets/minecraft/lang -pn --indent "\t"')
