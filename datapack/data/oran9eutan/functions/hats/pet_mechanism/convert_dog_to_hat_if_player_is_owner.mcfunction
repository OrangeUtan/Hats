# Converts dog to a hat if it is owned by the Player executing this function
# @s: Dog beeing checked for conversion

# Check if the Owner matches the stored UUID of the player. 0 if matches, 1 otherwise
execute store result score @s hats.math run data modify storage hats uuid set from entity @s Owner

# Convert dog to hat if the Player is the Owner
execute if score @s hats.math matches 0 run function oran9eutan:hats/pet_mechanism/convert_dog_to_hat
