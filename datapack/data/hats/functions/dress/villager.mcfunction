# as: The Villager beeing dressed
# descr: Dress the Villager with a random hat and give it hat trades

# Add optional favorite cat hat
execute if predicate hats:villager/chance_has_fav_cat run function hats:dress/villager_fav_cat

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