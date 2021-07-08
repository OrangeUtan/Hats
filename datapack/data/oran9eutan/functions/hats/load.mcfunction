# Initialises the datapack
# @: World

function oran9eutan:hats/init_scoreboards
function oran9eutan:hats/cfg/init

# Install datapack if it is not already
execute unless data storage minecraft:oran9eutan.hats {"version":{"major": 2, "minor": 3, "patch": 1}} run function oran9eutan:hats/install

#Start looping functions
execute if {{ hats.setting["pet_conversion"].is_true }} run function oran9eutan:hats/loops/can_player_convert_pets
execute if {{ hats.setting["dress_mobs"].is_true }} run function oran9eutan:hats/loops/dress_mobs
