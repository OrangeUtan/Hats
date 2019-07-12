###################################################
# Dresses Villager with a hat and adds hat trades #
###################################################

#----------------------#
# Add optional cat hat #
#----------------------#

scoreboard players set #hats_rand hats_range_up 47
function hats:calc_rand_num

# Equip Villager with a random cat hat, or none
execute if score #hats_rand hats_rand_num matches 1 run function hats:equip/cats/tabby
execute if score #hats_rand hats_rand_num matches 2 run function hats:equip/cats/tuxedo
execute if score #hats_rand hats_rand_num matches 3 run function hats:equip/cats/red
execute if score #hats_rand hats_rand_num matches 4 run function hats:equip/cats/siamese
execute if score #hats_rand hats_rand_num matches 5 run function hats:equip/cats/british_shorthair
execute if score #hats_rand hats_rand_num matches 6 run function hats:equip/cats/calico
execute if score #hats_rand hats_rand_num matches 7 run function hats:equip/cats/persian
execute if score #hats_rand hats_rand_num matches 8 run function hats:equip/cats/ragdoll
execute if score #hats_rand hats_rand_num matches 9 run function hats:equip/cats/white
execute if score #hats_rand hats_rand_num matches 10 run function hats:equip/cats/jellie
execute if score #hats_rand hats_rand_num matches 11 run function hats:equip/cats/black

# If Villagers has a cat hat, modify helmet drop chances
execute if score #hats_rand hats_rand_num matches 1..11 run data modify entity @s ArmorDropChances[3] set value 0.0f

# If Villager has a cat hat, add that cat as a trade
execute as @s if score #hats_rand hats_rand_num matches 1..11 run function hats:add_trades/favorite_cat

#-----------------------------------------------------#
# Give Villager special trade depending on profession #
#-----------------------------------------------------#

execute as @s[nbt={VillagerData:{profession:"minecraft:librarian"}}] run function hats:add_trades/librarian

#------------------------------------------------#
# Only tag villagers with professions as dressed #
#------------------------------------------------#
tag @s add hats_is_dressed