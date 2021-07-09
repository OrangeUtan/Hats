# Converts a pet into a hat and stores its data in the hat
# @s: Pet beeing converted to a hat

# Remove 1 lead from the players inventory
clear @p[tag=!global.ignore,distance=..0.001] lead 1

# Play conversion effects
execute at @s positioned ~ ~.3 ~ run particle minecraft:heart ~ ~ ~ 0.1 0.1 0.1 .001 1
execute if entity @s[type=wolf] at @s run playsound minecraft:entity.wolf.pant neutral @a[tag=!global.ignore] ~ ~ ~
execute if entity @s[type=cat] at @s run playsound minecraft:entity.cat.purr neutral @a[tag=!global.ignore] ~ ~ ~

# Give executing Player a pet hat
execute if entity @s[type=wolf] run loot give @p[tag=!global.ignore,distance=..0.001] loot oran9eutan:hats/hat_from/dog
execute if entity @s[type=cat] run loot give @p[tag=!global.ignore,distance=..0.001] loot oran9eutan:hats/hat_from/cat
execute at @s run function oran9eutan:hats/utils/remove_entity_silently
