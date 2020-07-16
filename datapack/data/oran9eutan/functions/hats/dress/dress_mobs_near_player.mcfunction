# executor: Player
# descr: Tries to dress all undressed mobs near the player

execute as @e[type=zombie,tag=!global.ignore,distance=0..64,tag=!hats.mob.dont_dress,predicate=!oran9eutan:hats/entity/wears_helmet] at @s run function oran9eutan:hats/dress/zombie
execute as @e[type=husk,tag=!global.ignore,distance=0..64,tag=!hats.mob.dont_dress,predicate=!oran9eutan:hats/entity/wears_helmet] at @s run function oran9eutan:hats/dress/husk
execute as @e[type=skeleton,tag=!global.ignore,distance=0..64,tag=!hats.mob.dont_dress,predicate=!oran9eutan:hats/entity/wears_helmet] at @s run function oran9eutan:hats/dress/skeleton
execute as @e[type=drowned,tag=!global.ignore,distance=0..64,tag=!hats.mob.dont_dress,predicate=!oran9eutan:hats/entity/wears_helmet] at @s run function oran9eutan:hats/dress/drowned
execute as @e[type=stray,tag=!global.ignore,distance=0..64,tag=!hats.mob.dont_dress,predicate=!oran9eutan:hats/entity/wears_helmet] at @s run function oran9eutan:hats/dress/stray
execute as @e[type=wandering_trader,tag=!global.ignore,distance=0..64,tag=!hats.mob.dont_dress,predicate=!oran9eutan:hats/entity/wears_helmet] at @s run function oran9eutan:hats/dress/wandering_trader
execute as @e[type=vindicator,tag=!global.ignore,distance=0..64,tag=!hats.mob.dont_dress,predicate=!oran9eutan:hats/entity/wears_helmet] at @s run function oran9eutan:hats/dress/vindicator

# Only dress Villagers with a profession
execute as @e[type=villager,tag=!global.ignore,distance=0..64,tag=!hats.mob.dont_dress,predicate=oran9eutan:hats/villager/has_profession] at @s run function oran9eutan:hats/dress/villager