from dataclasses import dataclass


@dataclass
class HatsOptions:
    cmd_id: int
    default_item_head: str
    default_item_inventory: str

    @classmethod
    def from_json(cls, json: dict):
        return HatsOptions(
            cmd_id=int(json["cmd_id"]),
            default_item_head=json["default_item_head"],
            default_item_inventory=json["default_item_inventory"],
        )
