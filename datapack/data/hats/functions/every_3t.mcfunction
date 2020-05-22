# Replace helmet hats on armorstands with stick hats
execute as @a at @s as @e[distance=0..10, type=minecraft:armor_stand,nbt={ArmorItems:[{},{},{},{id:"minecraft:leather_helmet",tag:{Tags:["is_hat"]}}]}] run function hats:hat_behavior/equip_armorstand_with_correct_hat

schedule function hats:every_3t 3t