# Adds offer of the favorite cat the Villager Trader is wearing
# @s: Villager beeing dressed

# Add template offer
data modify entity @s Offers.Recipes append value {sell:{id:"{{ hats.default_item_inventory }}",Count:1b}}

# Set the sell item of the template offer to the cat hat on the villagers head
data modify entity @s Offers.Recipes[-1].sell.tag set from entity @s ArmorItems[3].tag

# Set offer price
loot replace entity @s weapon.offhand loot oran9eutan:hats/trades/villager/fav_cat_price
data modify entity @s Offers.Recipes[-1].buy set from entity @s HandItems[1]
