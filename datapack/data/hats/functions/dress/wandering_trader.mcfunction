# as: The Wandering Trader beeing dressed
# Descr: Dress the Wandering Trader with a random hat and give it hat trades

# Add optional favorite cat hat
execute if predicate hats:wandering_trader/chance_has_fav_cat run function hats:dress/wandering_trader/add_fav_cat

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