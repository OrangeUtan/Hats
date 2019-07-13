###################################################
# Dresses Villager with a hat and adds hat trades #
###################################################

#----------------------#
# Add optional cat hat #
#----------------------#

# Equip Villager with random cat (or none)
loot replace entity @s armor.head loot hats:dress_mobs/villager

# If Villagers has a cat hat, modify helmet drop chances
execute if data entity @s ArmorItems[3].id run data modify entity @s ArmorDropChances[3] set value 0.0f

# If Villager has a cat hat, add that cat as a trade
execute if data entity @s ArmorItems[3].id run function hats:add_trades/favorite_cat

#-----------------------------------------------------#
# Give Villager special trade depending on profession #
#-----------------------------------------------------#

execute as @s[nbt={VillagerData:{profession:"minecraft:librarian"}}] run function hats:add_trades/librarian

#------------------------------------------------#
# Only tag villagers with professions as dressed #
#------------------------------------------------#
tag @s add hats_is_dressed