##############################################################################
# as: Wandering Trader                                                       #
# from: hats:dress_mobs_with_hats                                            #
# Descr: Dress the Wandering Trader with a random hat and give it hat trades #
##############################################################################

#----------------------#
# Add optional cat hat #
#----------------------#

# Equip Wandering Trader with random cat (or none)
loot replace entity @s armor.head loot hats:dress_mobs/wandering_trader

# If Wandering Trader has a cat hat, modify helmet drop chances
execute if data entity @s ArmorItems[3].id run data modify entity @s ArmorDropChances[3] set value 0.0f

# If Wandering Trader has a cat hat, add that cat as a trade
execute if data entity @s ArmorItems[3].id run function hats:add_trades/favorite_cat

#----------------------------------------------#
# Give Wandering Trader optional special trade #
#----------------------------------------------#

# Give Wandering Trader random special sell item (or none)
loot replace entity @s weapon.offhand loot hats:trades/wandering_trader

# Add special offer if Wandering Trader is holding a special item
execute as @s[nbt={HandItems:[{},{tag:{Tags:["is_hat"]}}]}] run function hats:add_trades/special

#----------------------------------#
# Mark Wandering Trader as dressed #
#----------------------------------#

tag @s add hats_is_dressed