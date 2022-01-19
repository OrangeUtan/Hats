# Adds profession dependent special offer to the Villager
# @s: Villager beeing dressed

# Add template offer
data modify entity @s Offers.Recipes append value {buy:{id:"minecraft:emerald", Count:1b}, sell:{id:"{{ hats.default_item_inventory }}",Count:1b}}

# Give Villager item depending on profession
loot replace entity @s weapon.offhand loot oran9eutan:hats/trades/villager/profession/_item
data modify entity @s Offers.Recipes[-1].sell.tag set from entity @s HandItems[1].tag

# Set offer price
loot replace entity @s weapon.offhand loot oran9eutan:hats/trades/villager/profession/_price
data modify entity @s Offers.Recipes[-1].buy set from entity @s HandItems[1]
