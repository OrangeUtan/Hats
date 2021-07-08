# Converts all nearby pets owned by a player into hats
# @s: Player trying to convert their pets to hats

# Store UUID of the Player
data modify storage hats uuid set from entity @s UUID

# Try to convert all nearby entities that have an owner
execute as @e[type=minecraft:wolf,tag=!global.ignore,distance=..2,predicate=oran9eutan:hats/entity/is_sitting] if data entity @s Owner run function oran9eutan:hats/pet_mechanism/convert_pet_to_hat_if_player_is_owner
