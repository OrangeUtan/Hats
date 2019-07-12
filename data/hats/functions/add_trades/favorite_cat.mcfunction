#####################################################
# Adds offer of the cat hat the Villager is wearing #
#####################################################

# Add template offer
data modify entity @s Offers.Recipes append value {buy:{id:"minecraft:emerald", Count:1b}, sell:{id:"minecraft:leather_helmet",Count:1b,tag:{CustomModelData:0,Tags:["is_hat"]}}}

# Set the sell item of the template offer to the cat hat on the villagers head
data modify entity @s Offers.Recipes[-1].sell.tag set from entity @s ArmorItems[3].tag

# Set random price
scoreboard players set #hats_rand hats_range_up 10
function hats:calc_rand_num

execute if score #hats_rand hats_rand_num matches 0 run data modify entity @s Offers.Recipes[-1].buy.Count set value 15
execute if score #hats_rand hats_rand_num matches 1 run data modify entity @s Offers.Recipes[-1].buy.Count set value 16
execute if score #hats_rand hats_rand_num matches 2 run data modify entity @s Offers.Recipes[-1].buy.Count set value 17
execute if score #hats_rand hats_rand_num matches 3 run data modify entity @s Offers.Recipes[-1].buy.Count set value 18
execute if score #hats_rand hats_rand_num matches 4 run data modify entity @s Offers.Recipes[-1].buy.Count set value 19
execute if score #hats_rand hats_rand_num matches 5 run data modify entity @s Offers.Recipes[-1].buy.Count set value 20
execute if score #hats_rand hats_rand_num matches 6 run data modify entity @s Offers.Recipes[-1].buy.Count set value 21
execute if score #hats_rand hats_rand_num matches 7 run data modify entity @s Offers.Recipes[-1].buy.Count set value 22
execute if score #hats_rand hats_rand_num matches 8 run data modify entity @s Offers.Recipes[-1].buy.Count set value 23
execute if score #hats_rand hats_rand_num matches 9 run data modify entity @s Offers.Recipes[-1].buy.Count set value 24