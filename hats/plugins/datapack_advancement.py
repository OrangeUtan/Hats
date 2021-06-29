from logging import getLogger

import jinja2
from beet import Context
from beet.library.data_pack import Advancement, DataPack

logger = getLogger(__name__)

CACHE_KEY = "datapack_advancement"


def beet_default(ctx: Context):
    namespace = ctx.meta["namespace"]
    config = ctx.meta["datapack_advancement"]
    author_head = config["author_head"]
    icon = config["icon"]

    cache = ctx.cache["hats"]
    if cache.has_changed("hats/plugins/datapack_advancement.py"):
        logger.info(f"Generating datapack advancement")
        data = _create_datapack_advancement(ctx, namespace, author_head, icon)
        data.save(path=cache.get_path(CACHE_KEY), overwrite=True)
    else:
        logger.info("Using cached datapack advancement")
        data = DataPack(path=cache.get_path(CACHE_KEY))

    ctx.data.merge(data)


def _create_datapack_advancement(ctx: Context, namespace: str, author_head: str, icon: dict):
    data = DataPack()

    env = jinja2.Environment(loader=jinja2.FileSystemLoader("hats/templates"))

    data.advancements[f"global:root"] = Advancement(
        env.get_template("advancements/datapack_root.json").render()
    )
    data.advancements[f"global:{ctx.project_author.lower()}"] = Advancement(
        env.get_template("advancements/datapack_author.json").render(
            author=ctx.project_author, author_head=author_head
        )
    )
    data.advancements[f"{namespace}/installed"] = Advancement(
        env.get_template("advancements/datapack_installed.json").render(
            name="Hats",
            version=f"v{ctx.project_version}",
            description=ctx.project_description,
            parent=f"global:{ctx.project_author.lower()}",
            icon=icon,
        )
    )

    return data
