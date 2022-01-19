# Checks every so often if any players are trying to convert a pet into a hat

# Convert pets near players that are trying to convert pets to hats
execute as @a[tag=!global.ignore] if predicate oran9eutan:hats/player/can_convert_pets at @s run function oran9eutan:hats/pet_mechanism/convert_pets_near_player

# Loop if enabled
execute if {{ hats.setting["pet_conversion"].is_true }} run schedule function oran9eutan:hats/loops/can_player_convert_pets 1s
