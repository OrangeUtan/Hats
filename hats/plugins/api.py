import json
from io import TextIOWrapper
from logging import getLogger
from pathlib import Path

from beet import Context

from hats.options import HatsOptions
from hats.registries.hats import HatRegistry

logger = getLogger(__name__)


def dataclasses_to_dicts(obj):
    """ Converts all nested dataclasses to dicts, if they implement a 'to_dict' mehtod """

    if isinstance(obj, (list, tuple, set)):
        return list(
            map(lambda e: e.to_dict() if hasattr(e, "to_dict") else dataclasses_to_dicts(e), obj)
        )
    elif isinstance(obj, dict):
        return dict(
            map(
                lambda i: (i[0], i[1].to_dict())
                if hasattr(i[1], "to_dict")
                else (i[0], dataclasses_to_dicts(i[1])),
                obj.items(),
            )
        )
    return obj


def remove_empty_fields(obj):
    """ Recursivley minimize object by removing empty lists and dict keys with value None """

    if isinstance(obj, (list, tuple, set)):
        return type(obj)(remove_empty_fields(x) for x in obj if x is not None)
    elif isinstance(obj, dict):
        obj = type(obj)(
            (remove_empty_fields(k), remove_empty_fields(v))
            for k, v in obj.items()
            if k is not None and v is not None
        )
        return type(obj)((k, v) for k, v in obj.items() if not (isinstance(v, list) and len(v) < 1))
    else:
        return obj


def dump_minimized_json(obj, file: TextIOWrapper):
    json.dump(
        remove_empty_fields(dataclasses_to_dicts(obj)), file, indent=None, separators=(",", ":")
    )


def generate_hats_registry(registry: HatRegistry, out: Path):
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w") as f:
        dump_minimized_json(registry.type_to_hat_map, f)


def generate_hats_by_category(registry: HatRegistry, out: Path):
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w") as f:
        dump_minimized_json(registry.categories, f)


API_DIR = Path("docs/api")


def beet_default(ctx: Context):
    opts = HatsOptions.from_json(ctx.meta["hats"])
    hats = HatRegistry.get(opts.cmd_id)

    generate_hats_registry(hats, API_DIR / "hats.json")
    generate_hats_by_category(hats, API_DIR / "hats_by_category.json")

    LANG_DIR = API_DIR / "lang"
    LANG_DIR.mkdir(exist_ok=True, parents=True)
    for lang, translations in ctx.assets.languages.items():
        lang_key = lang.removeprefix("minecraft:")
        with (LANG_DIR / f"{lang_key}.json").open("w") as f:
            dump_minimized_json(translations.data, f)
