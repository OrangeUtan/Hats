# executor: Wandering Trader beeing dressed
# descr: Adds a hat trade related to Villagers

# Add template offer that is modified later
data modify entity @s Offers.Recipes append value {buy:{id:"minecraft:emerald", Count:1b}, sell:{id:"minecraft:leather_helmet",Count:1b}}

# Give trade sell item
loot replace entity @s weapon.offhand loot oran9eutan:hats/hat_on_head/villager/random
data modify entity @s Offers.Recipes[-1].sell.tag set from entity @s HandItems[1].tag

# Set offer price
loot replace entity @s weapon.offhand loot oran9eutan:hats/trades/wandering_trader/villager_price
data modify entity @s Offers.Recipes[-1].buy set from entity @s HandItems[1]
