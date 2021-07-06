from dataclasses import dataclass


@dataclass
class HatsOptions:
    cmd_id: int

    @classmethod
    def from_json(cls, json: dict):
        return HatsOptions(cmd_id=int(json["cmd_id"]))
