# executor: Player
# descr: Tries to dress all undressed mobs near the player

execute as @e[tag=!global.ignore,type=zombie,distance=0..64,tag=!hats.mob.dont_dress,nbt=!{ArmorItems:[{},{},{},{Count:1b}]}] at @s run function oran9eutan:hats/dress/zombie
execute as @e[tag=!global.ignore,type=husk,distance=0..64,tag=!hats.mob.dont_dress,nbt=!{ArmorItems:[{},{},{},{Count:1b}]}] at @s run function oran9eutan:hats/dress/husk
execute as @e[tag=!global.ignore,type=skeleton,distance=0..64,tag=!hats.mob.dont_dress,nbt=!{ArmorItems:[{},{},{},{Count:1b}]}] at @s run function oran9eutan:hats/dress/skeleton
execute as @e[tag=!global.ignore,type=drowned,distance=0..64,tag=!hats.mob.dont_dress,nbt=!{ArmorItems:[{},{},{},{Count:1b}]}] at @s run function oran9eutan:hats/dress/drowned
execute as @e[tag=!global.ignore,type=stray,distance=0..64,tag=!hats.mob.dont_dress,nbt=!{ArmorItems:[{},{},{},{Count:1b}]}] at @s run function oran9eutan:hats/dress/stray
execute as @e[tag=!global.ignore,type=wandering_trader,distance=0..64,tag=!hats.mob.dont_dress] at @s run function oran9eutan:hats/dress/wandering_trader
execute as @e[tag=!global.ignore,type=minecraft:vindicator,distance=0..64,tag=!hats.mob.dont_dress,nbt=!{ArmorItems:[{},{},{},{Count:1b}]}] at @s run function oran9eutan:hats/dress/vindicator

# Only dress Villagers with a profession
execute as @e[tag=!global.ignore,type=villager,distance=0..64,tag=!hats.mob.dont_dress,nbt=!{VillagerData:{profession:"minecraft:none"}}] at @s run function oran9eutan:hats/dress/villager