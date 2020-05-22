# as: The Villager beeing dressed
# descr: Dress the Villager with a random hat and give it hat trades

#----------------------#
# Add optional cat hat #
#----------------------#

# Equip Villager with random cat (or none)
loot replace entity @s armor.head loot hats:dress/villager

# If Villagers has a cat hat, modify helmet drop chances
execute if data entity @s ArmorItems[3].id run data modify entity @s ArmorDropChances[3] set value 0.0f

# If Villager has a cat hat, add that cat as a trade
execute if data entity @s ArmorItems[3].id run function hats:add_trades/favorite_cat

#-------------------------------------------------------------#
# Give Villager optinal special trade depending on profession #
#-------------------------------------------------------------#

# Give Villager random special sell item (or none) depending on profession
execute as @s[nbt={VillagerData:{profession:"minecraft:librarian"}}] run loot replace entity @s weapon.offhand loot hats:trades/librarian
execute as @s[nbt={VillagerData:{profession:"minecraft:armorer"}}] run loot replace entity @s weapon.offhand loot hats:trades/armorer
execute as @s[nbt={VillagerData:{profession:"minecraft:farmer"}}] run loot replace entity @s weapon.offhand loot hats:trades/farmer
execute as @s[nbt={VillagerData:{profession:"minecraft:toolsmith"}}] run loot replace entity @s weapon.offhand loot hats:trades/toolsmith

# Add special offer if Villager is holding a special item
execute as @s[nbt={HandItems:[{},{tag:{Tags:["is_hat"]}}]}] run function hats:add_trades/special

#--------------------------#
# Mark Villager as dressed #
#--------------------------#
tag @s add hats.mob.dont_dress