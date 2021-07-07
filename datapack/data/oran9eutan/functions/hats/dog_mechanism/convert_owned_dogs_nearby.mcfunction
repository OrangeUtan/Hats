# Converts all nearby dogs owned by a Player into dog hats
# @s: Player whos dogs are going to be converted

# Store UUID of the Player
data modify storage hats uuid set from entity @s UUID

# Try to convert all nearby dogs that have an Owner
execute as @e[tag=!global.ignore,type=minecraft:wolf,distance=..2,predicate=oran9eutan:hats/entity/is_sitting] if data entity @s Owner run function oran9eutan:hats/dog_mechanism/convert_dog_to_hat_if_player_is_owner
