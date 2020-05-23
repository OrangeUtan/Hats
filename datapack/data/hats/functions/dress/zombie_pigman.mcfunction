# as: The Zombie Pigman beeing dressed
# descr: Dress the Zombie Pigman with a hat

loot replace entity @s armor.head loot hats:dress/zombie_pigman

execute as @s[nbt={ArmorItems:[{},{},{},{Count:1b}]}] run data modify entity @s ArmorDropChances[3] set value 1.0f
tag @s add hats.mob.dont_dress