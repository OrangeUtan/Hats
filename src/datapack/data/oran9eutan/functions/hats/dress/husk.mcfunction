# Try dressing a Husk with a hat
# @s: The Husk beeing dressed

execute if predicate oran9eutan:hats/chance_hostile_mob_has_hat run loot replace entity @s armor.head loot oran9eutan:hats/dress/husk
execute if predicate oran9eutan:hats/entity/wears_helmet run data modify entity @s ArmorDropChances[3] set value 1.0f

tag @s add hats.mob.dont_dress
