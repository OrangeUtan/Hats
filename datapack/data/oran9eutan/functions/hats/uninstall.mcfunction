# descr: Remove all Hats related from the world

# Goodbye
tellraw @a[tag=!global.ignore,tag=!global.ignore.gui] ["",{"text":"Uninstalling ","color":"gold"},{"text":"Hats ","color":"red"},{"text":"datapack version ","color":"gold"},{"score":{"name":"#installed_version","objective":"hats.cfg"},"color":"red"}]

# Remove scoreboards
scoreboard objectives remove hats.math
scoreboard objectives remove hats.cfg
scoreboard objectives remove hats.dropLthrHlm
scoreboard objectives remove hats.dropStick
scoreboard objectives remove hats.fix_old_hat

# Remove storage
data remove storage minecraft:hats buffer
data remove storage minecraft:hats dog_data
data remove storage minecraft:hats hat_to_fix

# Remove advancements
advancement revoke @a from hats:root