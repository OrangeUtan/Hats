from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Optional

import yaml


class SettingType(Enum):
    BOOL = "bool"

    @staticmethod
    def from_str(value: str):
        return {SettingType.BOOL.value: SettingType.BOOL}[value]


@dataclass(unsafe_hash=True)
class Setting:
    id: str
    title: str
    description: str
    type: SettingType
    default: Optional[Any]
    on_enable: Optional[str]
    on_disable: Optional[str]

    @property
    def scoreboard_holder(self):
        return f"#cfg.{self.id}"

    @classmethod
    def from_json(cls, id: str, json: dict):
        return Setting(
            id,
            json["title"],
            json["description"],
            SettingType.from_str(json["type"]),
            json.get("default"),
            json.get("on_enable"),
            json.get("on_disable"),
        )


@dataclass
class Section:
    id: str
    title: str
    settings: dict[str, Setting]

    MAX_LINES = 18

    @classmethod
    def from_json(cls, id: str, json: dict):
        return Section(
            id,
            json["title"],
            dict(map(lambda s: (s[0], Setting.from_json(s[0], s[1])), json["settings"].items())),
        )

    def section_root(self, namespace: str):
        return f"{namespace}/cfg/{self.id}"

    def main_function(self, namespace: str):
        return f"{self.section_root(namespace)}/main"


class SettingsRegistry:
    PATH = Path("src/settings.yml")

    def __init__(
        self,
        main_section: Section,
        sections: dict[str, Section],
        settings: dict[str, Setting],
        scoreboard: str,
    ):
        self.settings = settings
        self.sections = sections
        self.scoreboard = scoreboard
        self.main_section = main_section

    @classmethod
    def from_json(cls, json: dict):
        sections = {s[0]: Section.from_json(s[0], s[1]) for s in json["sections"].items()}

        settings = {}
        for section in sections.values():
            settings.update(section.settings)

        return SettingsRegistry(sections[json["main"]], sections, settings, json["scoreboard"])

    @classmethod
    def get(cls):
        with cls.PATH.open("r") as f:
            return cls.from_json(yaml.safe_load(f))

    def main_function(self, namespace: str):
        return f"{self.main_section.main_function(namespace)}"
