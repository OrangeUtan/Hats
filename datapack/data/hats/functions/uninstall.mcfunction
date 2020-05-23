# descr: Remove all Hats related from the world

# Remove Scoreboards
# scoreboard objectives remove hats_math

# Remove storage
data remove storage minecraft:hats buffer

# Remove advancements
advancement revoke @a from hats:root

# Goodbye
tellraw @s {"text":"Uninstalled Hats Datapack. Items have to be removed manually","color":"dark_red"}