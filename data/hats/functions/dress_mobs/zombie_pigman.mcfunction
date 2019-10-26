####################################################
# as: Zombie Pigman                                #
# from: hats:dress_mobs_with_hats                  #
# Descr: Dress the Zombie Pigman with a random hat #
####################################################

loot replace entity @s armor.head loot hats:dress_mobs/zombie_pigman

execute as @s[nbt={ArmorItems:[{},{},{},{Count:1b}]}] run data modify entity @s ArmorDropChances[3] set value 1.0f
tag @s add hats.mob.dont_dress