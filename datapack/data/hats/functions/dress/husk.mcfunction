# as: The Husk beeing dressed
# descr: Try dressing a Husk with a hat

loot replace entity @s armor.head loot hats:dress/husk

execute as @s[nbt={ArmorItems:[{},{},{},{Count:1b}]}] run data modify entity @s ArmorDropChances[3] set value 1.0f
tag @s add hats.mob.dont_dress