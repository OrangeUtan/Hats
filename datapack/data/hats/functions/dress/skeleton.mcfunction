# as: The Skeleton beeing dressed
# descr: Try dressing a Skeleton with a hat

loot replace entity @s armor.head loot hats:dress/skeleton

execute as @s[nbt={ArmorItems:[{},{},{},{Count:1b}]}] run data modify entity @s ArmorDropChances[3] set value 1.0f
tag @s add hats.mob.dont_dress