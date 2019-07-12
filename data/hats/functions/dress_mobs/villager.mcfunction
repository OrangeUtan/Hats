###################################################
# Dresses Villager with a hat and adds hat trades #
###################################################

#----------------------#
# Add optional cat hat #
#----------------------#

scoreboard players set @s hats_range_up 37
function hats:calc_rand_num

# Equip Villager with a random cat hat, or none
execute as @s[scores={hats_rand_num=1}] run function hats:equip/cats/tabby
execute as @s[scores={hats_rand_num=2}] run function hats:equip/cats/tuxedo
execute as @s[scores={hats_rand_num=3}] run function hats:equip/cats/red
execute as @s[scores={hats_rand_num=4}] run function hats:equip/cats/siamese
execute as @s[scores={hats_rand_num=5}] run function hats:equip/cats/british_shorthair
execute as @s[scores={hats_rand_num=6}] run function hats:equip/cats/calico
execute as @s[scores={hats_rand_num=7}] run function hats:equip/cats/persian
execute as @s[scores={hats_rand_num=8}] run function hats:equip/cats/ragdoll
execute as @s[scores={hats_rand_num=9}] run function hats:equip/cats/white
execute as @s[scores={hats_rand_num=10}] run function hats:equip/cats/jellie
execute as @s[scores={hats_rand_num=11}] run function hats:equip/cats/black

# If Villagers has a cat hat, modify helmet drop chances
execute as @s[scores={hats_rand_num=1..11}] run data modify entity @s ArmorDropChances[3] set value 0.0f

# If Villager has a cat hat, add that cat as a trade
execute as @s[scores={hats_rand_num=1..11}] run function hats:add_trades/favorite_cat

#-----------------------------------------------------#
# Give Villager special trade depending on profession #
#-----------------------------------------------------#

execute as @s[nbt={VillagerData:{profession:"minecraft:librarian"}}] run function hats:add_trades/librarian

#------------------------------------------------#
# Only tag villagers with professions as dressed #
#------------------------------------------------#
tag @s add hats_is_dressed