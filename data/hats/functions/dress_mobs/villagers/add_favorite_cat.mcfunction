# Created by Oran9eUtan

#------------------------------------------------------#
# Equips the Villager with the hat of its favorite cat.#
# Villager also offers their favorite cat.             #
#------------------------------------------------------#

scoreboard players set @s hats_range_up 37
function hats:calc_rand_num

execute as @s[scores={hats_rand_num=1}] run function hats:equip/cats/tabby
execute as @s[scores={hats_rand_num=2}] run function hats:equip/cats/tuxedo
execute as @s[scores={hats_rand_num=3}] run function hats:equip/cats/red
execute as @s[scores={hats_rand_num=4}] run function hats:equip/cats/siamese
execute as @s[scores={hats_rand_num=5}] run function hats:equip/cats/british_shorthair
execute as @s[scores={hats_rand_num=6}] run function hats:equip/cats/calico
execute as @s[scores={hats_rand_num=7}] run function hats:equip/cats/persian
execute as @s[scores={hats_rand_num=8}] run function hats:equip/cats/ragdoll
execute as @s[scores={hats_rand_num=9}] run function hats:equip/cats/white
execute as @s[scores={hats_rand_num=10}] run function hats:equip/cats/jellie
execute as @s[scores={hats_rand_num=11}] run function hats:equip/cats/black

# Add dummy offer
execute as @s[scores={hats_rand_num=1..11}] run data modify entity @s Offers.Recipes append value {buy:{id:"minecraft:emerald", Count:1b}, sell:{id:"minecraft:leather_helmet",Count:1b,tag:{Tags:["is_hat"]}}}

execute as @s[scores={hats_rand_num=1}] run data modify entity @s Offers.Recipes[-1].sell.tag merge value {CustomModelData:3121, display:{Name:'{"translate": "item.hats.cats.tabby.name"}'}}
execute as @s[scores={hats_rand_num=2}] run data modify entity @s Offers.Recipes[-1].sell.tag merge value {CustomModelData:3122, display:{Name:'{"translate": "item.hats.cats.tuxedo.name"}'}}
execute as @s[scores={hats_rand_num=3}] run data modify entity @s Offers.Recipes[-1].sell.tag merge value {CustomModelData:3123, display:{Name:'{"translate": "item.hats.cats.red.name"}'}}
execute as @s[scores={hats_rand_num=4}] run data modify entity @s Offers.Recipes[-1].sell.tag merge value {CustomModelData:3124, display:{Name:'{"translate": "item.hats.cats.siamese.name"}'}}
execute as @s[scores={hats_rand_num=5}] run data modify entity @s Offers.Recipes[-1].sell.tag merge value {CustomModelData:3125, display:{Name:'{"translate": "item.hats.cats.british_shorthair.name"}'}}
execute as @s[scores={hats_rand_num=6}] run data modify entity @s Offers.Recipes[-1].sell.tag merge value {CustomModelData:3126, display:{Name:'{"translate": "item.hats.cats.calico.name"}'}}
execute as @s[scores={hats_rand_num=7}] run data modify entity @s Offers.Recipes[-1].sell.tag merge value {CustomModelData:3127, display:{Name:'{"translate": "item.hats.cats.persian.name"}'}}
execute as @s[scores={hats_rand_num=8}] run data modify entity @s Offers.Recipes[-1].sell.tag merge value {CustomModelData:3128, display:{Name:'{"translate": "item.hats.cats.ragdoll.name"}'}}
execute as @s[scores={hats_rand_num=9}] run data modify entity @s Offers.Recipes[-1].sell.tag merge value {CustomModelData:3129, display:{Name:'{"translate": "item.hats.cats.white.name"}'}}
execute as @s[scores={hats_rand_num=10}] run data modify entity @s Offers.Recipes[-1].sell.tag merge value {CustomModelData:3130, display:{Name:'{"translate": "item.hats.cats.jellie.name"}'}}
execute as @s[scores={hats_rand_num=11}] run data modify entity @s Offers.Recipes[-1].sell.tag merge value {CustomModelData:3131, display:{Name:'{"translate": "item.hats.cats.black.name"}'}}

execute as @s[scores={hats_rand_num=1..11}] run data modify entity @s ArmorDropChances[3] set value 0.0f