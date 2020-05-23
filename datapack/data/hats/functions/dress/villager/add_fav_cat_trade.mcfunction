# executor: Villager beeing dressed
# Descr: Adds offer of the favorite cat the Villager Trader is wearing

# Add template offer
data modify entity @s Offers.Recipes append value {buy:{id:"minecraft:emerald", Count:1b}, sell:{id:"minecraft:leather_helmet",Count:1b,tag:{CustomModelData:0,Tags:["is_hat"]}}}

# Set the sell item of the template offer to the cat hat on the villagers head
data modify entity @s Offers.Recipes[-1].sell.tag set from entity @s ArmorItems[3].tag

#-----------------#
# Set offer price #
#-----------------#

# Random number in range [0,15]
scoreboard players set #hats_rng_range hats_math 16
function hats:math/rng
scoreboard players get #hats_rand_num hats_math

# Random number in range [15,30]
scoreboard players add #hats_rand_num hats_math 15

# Set price of last added offer to random number
execute store result entity @s Offers.Recipes[-1].buy.Count byte 1 run scoreboard players get #hats_rand_num hats_math