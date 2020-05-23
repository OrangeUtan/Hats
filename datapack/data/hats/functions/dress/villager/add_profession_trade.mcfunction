# executor: Villager beeing dressed
# descr: Adds profession dependent special offer to the Villager

# Add template offer
data modify entity @s Offers.Recipes append value {buy:{id:"minecraft:emerald", Count:1b}, sell:{id:"minecraft:leather_helmet",Count:1b}}

# Give Villager item depending on profession
loot replace entity @s weapon.offhand loot hats:trades/villager/profession
data modify entity @s Offers.Recipes[-1].sell.tag set from entity @s HandItems[1].tag

# Set offer price
loot replace entity @s weapon.offhand loot hats:trades/villager/special_price
data modify entity @s Offers.Recipes[-1].buy set from entity @s HandItems[1]