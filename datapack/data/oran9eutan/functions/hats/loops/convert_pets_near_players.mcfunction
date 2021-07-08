# Checks every so often if any players are trying to convert a pet into a hat

# Convert pets near players that are trying to convert pets to hats
execute as @a[tag=!global.ignore] at @s if predicate oran9eutan:hats/player/can_convert_pets if entity @e[tag=!global.ignore,type=minecraft:wolf,distance=..2,predicate=oran9eutan:hats/entity/is_sitting] run function oran9eutan:hats/pet_mechanism/convert_owned_pets_nearby

# Loop if enabled
execute if {{ hats.setting["pet_conversion"].is_true }} run schedule function oran9eutan:hats/loops/convert_pets_near_players 1s
