# Replace helmet hats on armorstands with stick hats
execute as @a[tag=!global.ignore] at @s as @e[tag=!global.ignore,distance=0..5, type=minecraft:armor_stand,nbt={ArmorItems:[{},{},{},{id:"minecraft:leather_helmet",tag:{Tags:["hats.hat"]}}]}] run function oran9eutan:hats/hat_mechanism/equip_armorstand_with_correct_hat

schedule function oran9eutan:hats/loops/replace_helmet_hats_on_armorstands 3t