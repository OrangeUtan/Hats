# as: The Wandering Trader beeing dressed
# Descr: Dress the Wandering Trader with a random hat and give it hat trades

#----------------------#
# Add optional cat hat #
#----------------------#

# Equip Wandering Trader with random cat (or none)
loot replace entity @s armor.head loot hats:dress/wandering_trader

# If Wandering Trader has a cat hat, modify helmet drop chances
execute if data entity @s ArmorItems[3].id run data modify entity @s ArmorDropChances[3] set value 0.0f

# If Wandering Trader has a cat hat, add that cat as a trade
execute if data entity @s ArmorItems[3].id run function hats:dress/villager/add_fav_cat_trade

#----------------------------------------------#
# Give Wandering Trader optional special trade #
#----------------------------------------------#

# Give Wandering Trader random special sell item (or none)
loot replace entity @s weapon.offhand loot hats:trades/wandering_trader

# Add special offer if Wandering Trader is holding a special item
execute as @s[nbt={HandItems:[{},{tag:{Tags:["is_hat"]}}]}] run function hats:dress/villager/add_special_trade

#----------------------------------#
# Mark Wandering Trader as dressed #
#----------------------------------#
tag @s add hats.mob.dont_dress