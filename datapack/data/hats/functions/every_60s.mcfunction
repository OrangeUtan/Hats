# Replace helmet hats on armorstands with stick hats
execute as @e[type=minecraft:armor_stand,nbt={ArmorItems:[{},{},{},{id:"minecraft:leather_helmet",tag:{Tags:["is_hat"]}}]}] run function hats:hat_mechanism/equip_armorstand_with_correct_hat

schedule function hats:every_60s 60s