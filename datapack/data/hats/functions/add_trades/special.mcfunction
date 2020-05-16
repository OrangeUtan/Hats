###################################################################################
# as: Villager/Wandering Trader                                                   #
# Descr: Adds profession dependent special offer to the Villager/Wandering Trader #
###################################################################################

# Add special offer
data modify entity @s Offers.Recipes append value {buy:{id:"minecraft:emerald", Count:1b}, sell:{id:"minecraft:leather_helmet",Count:1b,tag:{Tags:["is_hat"]}}}
data modify entity @s Offers.Recipes[-1].sell.tag merge from entity @s HandItems[1].tag

# Set random price
scoreboard players set @s hats_min_price 15
scoreboard players set @s hats_max_price 25

loot replace entity @s weapon.offhand loot hats:trades/rand_price
data modify entity @s Offers.Recipes[-1].buy.Count set from entity @s HandItems[1].Count

scoreboard players reset @s hats_min_price
scoreboard players reset @s hats_max_price

# Clean up
replaceitem entity @s weapon.offhand minecraft:air