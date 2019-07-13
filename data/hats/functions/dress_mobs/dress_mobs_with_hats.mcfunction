#####################################################
# Checks every x seconds if there are any new mobs. #
# If so, randomly dresses them with a hat (or none). #
######################################################

execute as @e[type=zombie,tag=!hats_is_dressed,nbt=!{ArmorItems:[{},{},{},{Count:1b}]}] at @s run function hats:dress_mobs/zombie
execute as @e[type=husk,tag=!hats_is_dressed,nbt=!{ArmorItems:[{},{},{},{Count:1b}]}] at @s run function hats:dress_mobs/husk
execute as @e[type=skeleton,tag=!hats_is_dressed,nbt=!{ArmorItems:[{},{},{},{Count:1b}]}] at @s run function hats:dress_mobs/skeleton
execute as @e[type=drowned,tag=!hats_is_dressed,nbt=!{ArmorItems:[{},{},{},{Count:1b}]}] at @s run function hats:dress_mobs/drowned
execute as @e[type=stray,tag=!hats_is_dressed,nbt=!{ArmorItems:[{},{},{},{Count:1b}]}] at @s run function hats:dress_mobs/stray
execute as @e[type=wandering_trader,tag=!hats_is_dressed] at @s run function hats:dress_mobs/wandering_trader

# Only dress Villagers with a profession
execute as @e[type=villager,tag=!hats_is_dressed,nbt=!{VillagerData:{profession:"minecraft:none"}}] at @s run function hats:dress_mobs/villager

# Schedule next check
schedule function hats:dress_mobs/dress_mobs_with_hats 5s