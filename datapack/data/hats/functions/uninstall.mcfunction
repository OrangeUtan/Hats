# descr: Remove all Hats related from the world

# Remove scoreboards
scoreboard objectives remove hatsMath
scoreboard objectives remove hatsConfig
scoreboard objectives remove hatsDrpdLthrHlmt
scoreboard objectives remove hatsDrpdStick

# Remove storage
data remove storage minecraft:hats buffer
data remove storage minecraft:hats dog_data

# Remove advancements
advancement revoke @a from hats:root

# Goodbye
tellraw @a ["",{"text":"Uninstalled ","color":"gold"},{"text":"Hats ","color":"red"},{"text":"datapack version ","color":"gold"},{"score":{"name":"#installed_version","objective":"hatsConfig"},"color":"red"}]