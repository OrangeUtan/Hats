# Created by Oran9eUtan

#-------------------#
# Add Glasses offer #
#-------------------#

# Add dummy offer
data modify entity @s Offers.Recipes append value {buy:{id:"minecraft:emerald", Count:1b}, sell:{id:"minecraft:leather_helmet",Count:1b,tag:{Tags:["is_hat"]}}}

# Set random sell item
scoreboard players set @s hats_range_up 3
function hats:calc_rand_num

execute as @s[scores={hats_rand_num=0}] run data modify entity @s Offers.Recipes[-1].sell.tag merge value {CustomModelData:3142, display:{Name:'{"translate": "item.hats.glasses.half_rim.name"}'}}
execute as @s[scores={hats_rand_num=1}] run data modify entity @s Offers.Recipes[-1].sell.tag merge value {CustomModelData:3143, display:{Name:'{"translate": "item.hats.glasses.rainbow.name"}'}}
execute as @s[scores={hats_rand_num=2}] run data modify entity @s Offers.Recipes[-1].sell.tag merge value {CustomModelData:3144, display:{Name:'{"translate": "item.hats.glasses.librarian.name"}'}}

# Set random price
scoreboard players set @s hats_range_up 4
function hats:calc_rand_num

execute as @s[scores={hats_rand_num=0}] run data modify entity @s Offers.Recipes[-1].buy.Count set value 4
execute as @s[scores={hats_rand_num=1}] run data modify entity @s Offers.Recipes[-1].buy.Count set value 5
execute as @s[scores={hats_rand_num=2}] run data modify entity @s Offers.Recipes[-1].buy.Count set value 6
execute as @s[scores={hats_rand_num=3}] run data modify entity @s Offers.Recipes[-1].buy.Count set value 7