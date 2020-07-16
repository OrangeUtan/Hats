# executor: The Zombie beeing dressed
# descr: Dress a Zombie with a hat 

# Try to make the Zombie a ghost
execute if predicate oran9eutan:hats/is_in_mansion if predicate oran9eutan:hats/is_dark_night if predicate oran9eutan:hats/chance_mob_is_ghost run function oran9eutan:hats/dress/mob_as_ghost

# Else try to give the Zombie a hat
execute as @s[tag=!hats.mob.is_ghost] if predicate oran9eutan:hats/chance_hostile_mob_has_hat run loot replace entity @s armor.head loot oran9eutan:hats/dress/zombie
execute as @s[tag=!hats.mob.is_ghost] if predicate oran9eutan:hats/entity/wears_helmet run data modify entity @s ArmorDropChances[3] set value 1.0f

tag @s add hats.mob.dont_dress