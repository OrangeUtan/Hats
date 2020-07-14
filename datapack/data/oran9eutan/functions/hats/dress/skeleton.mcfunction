# executor: The Skeleton beeing dressed
# descr: Try dressing a Skeleton with a hat

# Try to make the Skeleton a ghost
execute if predicate oran9eutan:hats/is_in_mansion if predicate oran9eutan:hats/is_dark_night if predicate oran9eutan:hats/chance_mob_is_ghost run function oran9eutan:hats/dress/mob_as_ghost

# Else try to give the Skeleton a hat
execute as @s[tag=!hats.mob.is_ghost] if predicate oran9eutan:hats/chance_hostile_mob_has_hat run loot replace entity @s armor.head loot hats:dress/skeleton
execute as @s[tag=!hats.mob.is_ghost] run data modify entity @s ArmorDropChances[3] set value 1.0f

tag @s add hats.mob.dont_dress