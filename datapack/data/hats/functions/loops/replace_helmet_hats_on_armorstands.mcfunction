# Replace helmet hats on armorstands with stick hats
execute as @a at @s as @e[distance=0..5, type=minecraft:armor_stand,nbt={ArmorItems:[{},{},{},{id:"minecraft:leather_helmet",tag:{Tags:["hats.hat"]}}]}] run function hats:hat_mechanism/equip_armorstand_with_correct_hat

schedule function hats:loops/replace_helmet_hats_on_armorstands 3t