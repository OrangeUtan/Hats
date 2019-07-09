# Created by Oran9eUtan

scoreboard players set @s hats_range_up 19
function hats:dress_mobs/calc_rand_num

# Misc
execute as @s[scores={hats_rand_num=1}] run function hats:equip/fez

# Tophats
execute as @s[scores={hats_rand_num=2}] run function hats:equip/tophats/yellow
execute as @s[scores={hats_rand_num=3}] run function hats:equip/tophats/lime
execute as @s[scores={hats_rand_num=4}] run function hats:equip/tophats/pink
execute as @s[scores={hats_rand_num=5}] run function hats:equip/tophats/gray

# Glasses
execute as @s[scores={hats_rand_num=6}] run function hats:equip/accessories/sunglasses

# Accessories
execute as @s[scores={hats_rand_num=7}] run function hats:equip/accessories/steve_mask
execute as @s[scores={hats_rand_num=8}] run function hats:equip/accessories/alex_mask
execute as @s[scores={hats_rand_num=9}] run function hats:equip/accessories/googly_eyes


execute as @s[nbt={ArmorItems:[{},{},{},{Count:1b}]}] run data modify entity @s ArmorDropChances[3] set value 1.0f
tag @s add hats_is_dressed