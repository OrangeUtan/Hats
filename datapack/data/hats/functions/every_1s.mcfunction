execute as @a at @s if predicate hats:player/is_sneaking if predicate hats:player/is_holding_dog_leash if entity @e[type=minecraft:wolf,distance=..2,nbt={Sitting:true}] run function hats:dog_mechanism/convert_owned_dogs_nearby

schedule function hats:every_1s 1s