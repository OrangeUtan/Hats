# A loop that checks every so often if any Players are trying to convert a dog into a hat

# Convert dogs near Players that are trying to convert dogs to hats
execute as @a at @s if predicate hats:player/is_sneaking if predicate hats:player/is_holding_dog_leash if entity @e[type=minecraft:wolf,distance=..2,nbt={Sitting:true}] run function hats:dog_mechanism/convert_owned_dogs_nearby

# Loop if enabled
# execute if score #ha hatsConfig matches 1 run schedule function hats:loops/convert_thrown_dog_hat_items
execute if score #opt_convert_dogs hatsConfig matches 1 run schedule function hats:loops/convert_thrown_dog_hat_items 1s