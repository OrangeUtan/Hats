# Created by Oran9eUtan

scoreboard players set @s hats_range_up 11
function hats:calc_rand_num

# Misc
execute as @s[scores={hats_rand_num=1}] run function hats:equip/squid

# Accessories
execute as @s[scores={hats_rand_num=2}] run function hats:equip/accessories/snorkel_mask_blue
execute as @s[scores={hats_rand_num=3}] run function hats:equip/accessories/snorkel_mask_red
execute as @s[scores={hats_rand_num=9}] run function hats:equip/accessories/googly_eyes

execute as @s[nbt={ArmorItems:[{},{},{},{Count:1b}]}] run data modify entity @s ArmorDropChances[3] set value 1.0f
tag @s add hats_is_dressed