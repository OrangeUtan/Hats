# descr: Remove all Hats related from the world

# Remove scoreboards
scoreboard objectives remove hatsMath
scoreboard objectives remove hatsDrpdLthrHlmt
scoreboard objectives remove hatsDrpdStick

# Remove storage
data remove storage minecraft:hats buffer

# Remove advancements
advancement revoke @a from hats:root

# Goodbye
tellraw @s {"text":"Uninstalled Hats Datapack. Items have to be removed manually","color":"dark_red"}