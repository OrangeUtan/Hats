# Created by Oran9eUtan

scoreboard players set @s hats_range_up 19
function hats:calc_rand_num

# Misc
execute as @s[scores={hats_rand_num=1}] run function hats:equip/arrow

# Tophats
execute as @s[scores={hats_rand_num=2}] run function hats:equip/tophats/light_gray
execute as @s[scores={hats_rand_num=3}] run function hats:equip/tophats/cyan
execute as @s[scores={hats_rand_num=4}] run function hats:equip/tophats/purple
execute as @s[scores={hats_rand_num=5}] run function hats:equip/tophats/blue

# Glasses
execute as @s[scores={hats_rand_num=6}] run function hats:equip/glasses/harry_potter

# Accessories
execute as @s[scores={hats_rand_num=7}] run function hats:equip/accessories/steve_mask
execute as @s[scores={hats_rand_num=8}] run function hats:equip/accessories/alex_mask
execute as @s[scores={hats_rand_num=9}] run function hats:equip/accessories/googly_eyes


execute as @s[nbt={ArmorItems:[{},{},{},{Count:1b}]}] run data modify entity @s ArmorDropChances[3] set value 1.0f
tag @s add hats_is_dressed