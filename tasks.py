from invoke import task


@task
def setup(c):
    c.run("poetry lock -n")
    c.run("poetry install -n")
    c.run("poetry run pre-commit install")


@task
def format(c):
    c.run("poetry run black . --config pyproject.toml")
    c.run("poetry run isort . --settings-path pyproject.toml")
