# Created by Oran9eUtan

scoreboard players set #hats_rand hats_range_up 31
function hats:calc_rand_num

# Misc
execute if score #hats_rand hats_rand_num matches 1 run function hats:equip/squid

# Accessories
execute if score #hats_rand hats_rand_num matches 2 run function hats:equip/accessories/snorkel_mask_blue
execute if score #hats_rand hats_rand_num matches 3 run function hats:equip/accessories/snorkel_mask_red
execute if score #hats_rand hats_rand_num matches 4 run function hats:equip/accessories/googly_eyes

execute as @s[nbt={ArmorItems:[{},{},{},{Count:1b}]}] run data modify entity @s ArmorDropChances[3] set value 1.0f
tag @s add hats_is_dressed