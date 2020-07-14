# Converts dog to a hat if it is owned by the Player executing this function
# executor: Dog beeing checked for conversion

#define score_holder #hats_is_valid Variable that indicates if a check is valid or not

# Assume next check is valid
scoreboard players set #hats_is_valid hatsMath 1

#region: Check if the Player is the dogs Owner by comparing the their UUID with the Owner
execute store result score @s hatsMath run data get entity @s Owner[0]
execute unless score @s hatsMath = #hats_uuid0 hatsMath run scoreboard players set #hats_is_valid hatsMath 0

execute store result score @s hatsMath run data get entity @s Owner[1]
execute unless score @s hatsMath = #hats_uuid1 hatsMath run scoreboard players set #hats_is_valid hatsMath 0

execute store result score @s hatsMath run data get entity @s Owner[2]
execute unless score @s hatsMath = #hats_uuid2 hatsMath run scoreboard players set #hats_is_valid hatsMath 0

execute store result score @s hatsMath run data get entity @s Owner[3]
execute unless score @s hatsMath = #hats_uuid3 hatsMath run scoreboard players set #hats_is_valid hatsMath 0
#endregion

# Convert dog to hat if the Player is the Owner
execute if score #hats_is_valid hatsMath matches 1 run function oran9eutan:hats/dog_mechanism/convert_dog_to_hat