# Created by Oran9eUtan

#-------------------#
# Add Glasses offer #
#-------------------#

# Add dummy offer
data modify entity @s Offers.Recipes append value {buy:{id:"minecraft:emerald", Count:1b}, sell:{id:"minecraft:leather_helmet",Count:1b,tag:{Tags:["is_hat"]}}}

# Set random sell item
scoreboard players set #hats_rand hats_range_up 3
function hats:calc_rand_num

execute if score #hats_rand hats_rand_num matches 0 run data modify entity @s Offers.Recipes[-1].sell.tag merge value {CustomModelData:3142, display:{Name:'{"translate": "item.hats.glasses.half_rim.name"}'}}
execute if score #hats_rand hats_rand_num matches 1 run data modify entity @s Offers.Recipes[-1].sell.tag merge value {CustomModelData:3143, display:{Name:'{"translate": "item.hats.glasses.rainbow.name"}'}}
execute if score #hats_rand hats_rand_num matches 2 run data modify entity @s Offers.Recipes[-1].sell.tag merge value {CustomModelData:3144, display:{Name:'{"translate": "item.hats.glasses.librarian.name"}'}}

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