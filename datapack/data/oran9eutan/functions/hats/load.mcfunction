# Initialises the datapack
# executor: World

# Install datapack if it is not already
scoreboard objectives add hats.cfg dummy
execute unless data storage minecraft:oran9eutan.hats {"version":{"major": 2, "minor": 3, "patch": 1}} run function oran9eutan:hats/install

#Start looping functions
execute if {{ hats.setting["dog_conversion"].is_true }} run function oran9eutan:hats/loops/convert_dogs_near_players
execute if {{ hats.setting["dress_mobs"].is_true }} run function oran9eutan:hats/loops/dress_mobs
