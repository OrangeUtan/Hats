# executor: Villager beeing dressed
# Descr: Adds offer of the favorite cat the Villager Trader is wearing

# Add template offer
data modify entity @s Offers.Recipes append value {buy:{id:"minecraft:emerald", Count:1b}, sell:{id:"minecraft:leather_helmet",Count:1b,tag:{CustomModelData:0,Tags:["is_hat"]}}}

# Set the sell item of the template offer to the cat hat on the villagers head
data modify entity @s Offers.Recipes[-1].sell.tag set from entity @s ArmorItems[3].tag

# Set random price
scoreboard players set @s hats_min_price 15
scoreboard players set @s hats_max_price 30

loot replace entity @s weapon.offhand loot hats:trades/rand_price
data modify entity @s Offers.Recipes[-1].buy.Count set from entity @s HandItems[1].Count

scoreboard players reset @s hats_min_price
scoreboard players reset @s hats_max_price