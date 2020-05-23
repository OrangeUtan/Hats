# executor: Player
# descr: Tries to dress all undressed mobs near the player

execute as @e[type=zombie,distance=0..64,tag=!hats.mob.dont_dress,nbt=!{ArmorItems:[{},{},{},{Count:1b}]}] at @s run function hats:dress/zombie
execute as @e[type=husk,distance=0..64,tag=!hats.mob.dont_dress,nbt=!{ArmorItems:[{},{},{},{Count:1b}]}] at @s run function hats:dress/husk
execute as @e[type=skeleton,distance=0..64,tag=!hats.mob.dont_dress,nbt=!{ArmorItems:[{},{},{},{Count:1b}]}] at @s run function hats:dress/skeleton
execute as @e[type=drowned,distance=0..64,tag=!hats.mob.dont_dress,nbt=!{ArmorItems:[{},{},{},{Count:1b}]}] at @s run function hats:dress/drowned
execute as @e[type=stray,distance=0..64,tag=!hats.mob.dont_dress,nbt=!{ArmorItems:[{},{},{},{Count:1b}]}] at @s run function hats:dress/stray
execute as @e[type=wandering_trader,distance=0..64,tag=!hats.mob.dont_dress] at @s run function hats:dress/wandering_trader
execute as @e[type=zombie_pigman,distance=0..64,tag=!hats.mob.dont_dress,nbt=!{ArmorItems:[{},{},{},{Count:1b}]}] at @s run function hats:dress/zombie_pigman

# Only dress Villagers with a profession
execute as @e[type=villager,distance=0..64,tag=!hats.mob.dont_dress,nbt=!{VillagerData:{profession:"minecraft:none"}}] at @s run function hats:dress/villager