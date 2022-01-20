import json
from logging import getLogger
from pathlib import Path

from beet import Context

from hats.options import HatsOptions
from hats.registries.hats import HatRegistry

logger = getLogger(__name__)

HATS_PATH = Path("docs/api/hats.json")


def remove_empty_fields(obj):
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


def beet_default(ctx: Context):
    opts = HatsOptions.from_json(ctx.meta["hats"])
    hats = HatRegistry.get(opts.cmd_id)

    HATS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with HATS_PATH.open("w") as f:
        j = {_type: hat.to_dict() for _type, hat in hats.type_to_hat_map.items()}
        json.dump(remove_empty_fields(j), f, indent=None, separators=(",", ":"))
