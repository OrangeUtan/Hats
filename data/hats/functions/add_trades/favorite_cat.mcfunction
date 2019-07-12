#####################################################
# Adds offer of the cat hat the Villager is wearing #
#####################################################

# Add template offer
execute as @s[scores={hats_rand_num=1..11}] run data modify entity @s Offers.Recipes append value {buy:{id:"minecraft:emerald", Count:1b}, sell:{id:"minecraft:leather_helmet",Count:1b,tag:{CustomModelData:0,Tags:["is_hat"]}}}

# Set the sell item of the template offer to the cat hat on the villagers head
data modify entity @s Offers.Recipes[-1].sell.tag set from entity @s ArmorItems[3].tag

# Set random price
scoreboard players set @s hats_range_up 10
function hats:calc_rand_num

execute as @s[scores={hats_rand_num=0}] run data modify entity @s Offers.Recipes[-1].buy.Count set value 15
execute as @s[scores={hats_rand_num=1}] run data modify entity @s Offers.Recipes[-1].buy.Count set value 16
execute as @s[scores={hats_rand_num=2}] run data modify entity @s Offers.Recipes[-1].buy.Count set value 17
execute as @s[scores={hats_rand_num=3}] run data modify entity @s Offers.Recipes[-1].buy.Count set value 18
execute as @s[scores={hats_rand_num=4}] run data modify entity @s Offers.Recipes[-1].buy.Count set value 19
execute as @s[scores={hats_rand_num=5}] run data modify entity @s Offers.Recipes[-1].buy.Count set value 20
execute as @s[scores={hats_rand_num=6}] run data modify entity @s Offers.Recipes[-1].buy.Count set value 21
execute as @s[scores={hats_rand_num=7}] run data modify entity @s Offers.Recipes[-1].buy.Count set value 22
execute as @s[scores={hats_rand_num=8}] run data modify entity @s Offers.Recipes[-1].buy.Count set value 23
execute as @s[scores={hats_rand_num=9}] run data modify entity @s Offers.Recipes[-1].buy.Count set value 24