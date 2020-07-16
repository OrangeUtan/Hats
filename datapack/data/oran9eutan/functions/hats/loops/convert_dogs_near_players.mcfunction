# A loop that checks every so often if any Players are trying to convert a dog into a hat

# Convert dogs near Players that are trying to convert dogs to hats
execute as @a[tag=!global.ignore] at @s if predicate oran9eutan:hats/player/is_sneaking if predicate oran9eutan:hats/player/is_holding_dog_leash if entity @e[tag=!global.ignore,type=minecraft:wolf,distance=..2,nbt={Sitting:true}] run function oran9eutan:hats/dog_mechanism/convert_owned_dogs_nearby

# Loop if enabled
execute if score #opt_convert_dogs hats.cfg matches 1 run schedule function oran9eutan:hats/loops/convert_dogs_near_players 1s