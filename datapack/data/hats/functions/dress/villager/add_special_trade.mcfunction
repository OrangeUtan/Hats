# executor: Villager beeing dressed
# descr: Adds profession dependent special offer to the Villager

# Add special offer
data modify entity @s Offers.Recipes append value {buy:{id:"minecraft:emerald", Count:1b}, sell:{id:"minecraft:leather_helmet",Count:1b,tag:{Tags:["is_hat"]}}}
data modify entity @s Offers.Recipes[-1].sell.tag merge from entity @s HandItems[1].tag

# Set offer price
loot replace entity @s weapon.offhand loot hats:trades/prices/villager_special
data modify entity @s Offers.Recipes[-1].buy set from entity @s HandItems[1]

# Clean up
replaceitem entity @s weapon.offhand minecraft:air