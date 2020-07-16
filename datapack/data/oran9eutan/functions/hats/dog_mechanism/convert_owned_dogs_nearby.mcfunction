# Converts all nearby dogs owned by a Player into dog hats
# executor: Player whos dogs are going to be converted

# Store UUID of the Player
execute store result score #hats_uuid0 hats.math run data get entity @s UUID[0]
execute store result score #hats_uuid1 hats.math run data get entity @s UUID[1]
execute store result score #hats_uuid2 hats.math run data get entity @s UUID[2]
execute store result score #hats_uuid3 hats.math run data get entity @s UUID[3]

# Try to convert all nearby dogs that have an Owner
execute as @e[type=minecraft:wolf,distance=..2,nbt={Sitting:true}] if data entity @s Owner run function oran9eutan:hats/dog_mechanism/convert_dog_to_hat_if_player_is_owner