import json
from logging import getLogger
from typing import Any, Optional

from beet import Context
from beet.library.data_pack import DataPack, Function, LootTable

from hats.registries.settings import Section, Setting, SettingsRegistry, SettingType

logger = getLogger(__name__)


def beet_default(ctx: Context):
    namespace = ctx.meta["namespace"]
    config = ctx.meta["hats"]
    registry = SettingsRegistry.get()

    config["setting"] = {
        s.id: {
            "is_true": f"score {s.scoreboard_holder} {registry.scoreboard} matches 1",
            "is_false": f"score {s.scoreboard_holder} {registry.scoreboard} matches 0",
        }
        for s in registry.settings.values()
    }

    create_chat_config(ctx, registry, namespace)
    ctx.data.loot_tables[f"{namespace}/cfg"] = create_config_book_loot_table(
        ctx, registry, namespace
    )
    ctx.data.functions[f"{namespace}/cfg_book"] = Function(
        ["loot give @s loot oran9eutan:hats/cfg"]
    )


def create_chat_config(ctx: Context, registry: SettingsRegistry, namespace: str):
    ctx.data.functions[f"{namespace}/cfg/init"] = create_init_settings_function(registry)

    for section in registry.sections.values():
        ctx.data.merge(create_section(section, registry, ctx.project_name, namespace))

    ctx.data.functions[f"{namespace}/cfg"] = Function(
        [f"function {registry.main_function(namespace)}", cmd_blank_line]
    )


def create_config_book_loot_table(ctx: Context, registry: SettingsRegistry, namespace: str):
    CHECK = "\u2714"
    CROSS = "\u00D7"
    LOOP = "\u27f2"

    pages = []
    for section in registry.sections.values():
        # Section header
        page = [f"{section.title}:\n"]

        # Interactive settings
        for setting in section.settings.values():
            if setting.type == SettingType.BOOL:
                enable_function = f"{section.section_root(namespace)}/enable_{setting.id}"
                disable_function = f"{section.section_root(namespace)}/disable_{setting.id}"
                reset_function = enable_function if setting.default else disable_function

                page += [
                    "- ",
                    textcomp_interactive(setting.title, hover_text=setting.description),
                    ": ",
                    textcomp_interactive(CHECK, "dark_green", "Enable", enable_function),
                    textcomp_interactive(CROSS, "red", "Disable", disable_function),
                    textcomp_interactive(f"{LOOP}\n", "aqua", "Reset", reset_function),
                ]

        pages.append(json.dumps(page))

    return LootTable(
        {
            "pools": [
                {
                    "rolls": 1,
                    "entries": [
                        {
                            "type": "minecraft:item",
                            "name": "minecraft:written_book",
                            "functions": [
                                {
                                    "function": "minecraft:set_nbt",
                                    "tag": f'{{title: "{ctx.project_name} Configuration", author: "{ctx.project_author}"}}',
                                },
                                {"function": "minecraft:set_nbt", "tag": f"{{pages:{pages}}}"},
                            ],
                        }
                    ],
                }
            ]
        }
    )


def textcomp_interactive(
    text: str,
    color: Optional[str] = None,
    hover_text: Optional[str] = None,
    on_click: Optional[str] = None,
):
    textcomp = {"text": text}

    if color:
        textcomp["color"] = color
    if hover_text:
        textcomp["hoverEvent"] = {"action": "show_text", "contents": hover_text}
    if on_click:
        textcomp["clickEvent"] = {"action": "run_command", "value": f"/function {on_click}"}

    return textcomp


def create_init_settings_function(registry: SettingsRegistry):
    lines = []
    for setting in registry.settings.values():
        if setting.type == SettingType.BOOL:
            lines.append(
                f"execute unless score {setting.scoreboard_holder} {registry.scoreboard} matches -2147483648.. run {cmd_set_score(setting.scoreboard_holder, registry.scoreboard, 1 if setting.default else 0)}"
            )

    return Function(lines)


def create_section(section: Section, registry: SettingsRegistry, project_name: str, namespace: str):
    data = DataPack()

    section_root = section.section_root(namespace)
    project_title = f"{project_name} config: "

    # Show header
    lines = [
        f'tellraw @s ["",{{"text":"{project_title}","color":"gold"}}, {{"text": "{section.title}"}}]',
        f"tellraw @s {{\"text\":\"{'-'*len(project_title)}\"}}",
    ]

    # List settings
    for setting in section.settings.values():
        lines += cmds_show_setting_config(setting, registry, section_root)
        data.functions[f"{section_root}/enable_{setting.id}"] = create_set_bool_setting_function(
            setting, registry.scoreboard, True, section_root
        )
        data.functions[f"{section_root}/disable_{setting.id}"] = create_set_bool_setting_function(
            setting, registry.scoreboard, False, section_root
        )

    # Fill chat window
    lines += [cmd_blank_line for _ in range(section.MAX_LINES - len(lines) + 2)]

    data.functions[section.main_function(namespace)] = Function(lines)
    return data


def create_set_bool_setting_function(
    setting: Setting, scoreboard: str, value: bool, section_root: str
):
    lines = [
        cmd_set_score(setting.scoreboard_holder, scoreboard, 1 if value else 0),
        f"function {section_root}/main",
    ]

    if value and setting.on_enable:
        lines.append(setting.on_enable)
    elif not value and setting.on_disable:
        lines.append(setting.on_disable)

    return Function(lines)


def textcomp_set_bool_setting(setting: Setting, value: bool, change_function: str):
    textcomp = {
        "text": setting.title,
        "clickEvent": {"action": "run_command", "value": f"/function {change_function}"},
        "hoverEvent": {"action": "show_text", "contents": setting.description},
    }

    if value:
        textcomp["strikethrough"] = True
        textcomp["color"] = "gray"

    return textcomp


def cmd_set_score(scoreboard_holder: str, scoreboard: str, value: int):
    return f"scoreboard players set {scoreboard_holder} {scoreboard} {value}"


def cmd_if_score(scoreboard_holder: str, scoreboard: str, value: int, then: Any):
    return f"execute as @s if score {scoreboard_holder} {scoreboard} matches {value} run {then}"


def cmds_show_setting_config(setting: Setting, registry: SettingsRegistry, section_root: str):
    if setting.type == SettingType.BOOL:
        textcomp_enable = textcomp_set_bool_setting(
            setting, True, f"{section_root}/enable_{setting.id}"
        )
        textcomp_disable = textcomp_set_bool_setting(
            setting, False, f"{section_root}/disable_{setting.id}"
        )

        return [
            cmd_if_score(
                setting.scoreboard_holder,
                registry.scoreboard,
                0,
                f'tellraw @s [{{"text": "- "}}, {json.dumps(textcomp_enable)}]',
            ),
            cmd_if_score(
                setting.scoreboard_holder,
                registry.scoreboard,
                1,
                f'tellraw @s [{{"text": "- "}}, {json.dumps(textcomp_disable)}]',
            ),
        ]


cmd_blank_line = f'tellraw @s [""]'
