# Converts a pet to a hat if it is owned by the player currently trying to convert his pet
# @s: Pet checking if it can be converted by the player

# Check if the owner matches the stored UUID of the player. 0 if matches, 1 otherwise
execute store result score @s hats.math run data modify storage hats uuid set from entity @s Owner

# Convert the pet to a hat if the player is the owner
execute if score @s hats.math matches 0 run function oran9eutan:hats/pet_mechanism/convert_pet_to_hat
