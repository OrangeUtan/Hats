# descr: Remove all Hats related from the world

# Goodbye
tellraw @a[tag=!global.ignore,tag=!global.ignore.gui] ["",{"text":"Uninstalling ","color":"gold"},{"text":"Hats ","color":"red"}, {"text": "v", "color": "red"}, {"storage": "oran9eutan.hats", "nbt": "version.major", "color":"red"}, {"text": ".","color":"red"}, {"storage": "oran9eutan.hats", "nbt": "version.minor", "color":"red"}, {"text": ".","color":"red"}, {"storage": "oran9eutan.hats", "nbt": "version.patch", "color":"red"}]

# Remove scoreboards
scoreboard objectives remove hats.math
scoreboard objectives remove hats.cfg
scoreboard objectives remove hats.dropLthrHlm
scoreboard objectives remove hats.drpWFOAS
scoreboard objectives remove hats.fix_old_hat

# Remove storage
data remove storage minecraft:hats buffer
data remove storage minecraft:hats pet_data
data remove storage minecraft:hats hat_to_fix
data remove storage minecraft:oran9eutan.hats version

# Remove advancements
advancement revoke @a from hats:root
