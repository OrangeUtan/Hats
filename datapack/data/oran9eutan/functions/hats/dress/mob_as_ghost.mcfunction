# Dresses a mob with a ghost hat and gives it invisibility
# @s: Mob that is going to be dressed as a ghost
# requires: @s must have ArmorItems nbt and a hat slot

loot replace entity @s armor.head loot oran9eutan:hats/hat_on_head/halloween/wiggly_ghast
data modify entity @s ArmorDropChances[3] set value 1.0f
effect give @s minecraft:invisibility 99999 1 true
tag @s add hats.mob.is_ghost
