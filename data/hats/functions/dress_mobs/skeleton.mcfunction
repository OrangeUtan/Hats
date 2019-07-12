# Created by Oran9eUtan

scoreboard players set #hats_rand hats_range_up 31
function hats:calc_rand_num

# Misc
execute if score #hats_rand hats_rand_num matches 1 run function hats:equip/arrow

# Tophats
execute if score #hats_rand hats_rand_num matches 2 run function hats:equip/tophats/light_gray
execute if score #hats_rand hats_rand_num matches 3 run function hats:equip/tophats/cyan
execute if score #hats_rand hats_rand_num matches 4 run function hats:equip/tophats/purple
execute if score #hats_rand hats_rand_num matches 5 run function hats:equip/tophats/blue

# Glasses
execute if score #hats_rand hats_rand_num matches 6 run function hats:equip/glasses/harry_potter

# Accessories
execute if score #hats_rand hats_rand_num matches 7 run function hats:equip/accessories/steve_mask
execute if score #hats_rand hats_rand_num matches 8 run function hats:equip/accessories/alex_mask
execute if score #hats_rand hats_rand_num matches 9 run function hats:equip/accessories/googly_eyes


execute as @s[nbt={ArmorItems:[{},{},{},{Count:1b}]}] run data modify entity @s ArmorDropChances[3] set value 1.0f
tag @s add hats_is_dressed