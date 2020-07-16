# executor: Drowned beeing dressed
# descr: Try dressing a Drowned with a hat

execute if predicate oran9eutan:hats/chance_hostile_mob_has_hat run loot replace entity @s armor.head loot oran9eutan:hats/dress/drowned
execute if predicate oran9eutan:hats/entity/wears_helmet run data modify entity @s ArmorDropChances[3] set value 1.0f

tag @s add hats.mob.dont_dress