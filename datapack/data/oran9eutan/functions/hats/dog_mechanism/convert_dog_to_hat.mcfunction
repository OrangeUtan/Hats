# Converts a dog into a dog hat and stores its data in the hat
# executor: Dog beeing converted to a hat

# Remove 1 lead from the players inventory
clear @p[tag=!global.ignore,distance=..0.001] lead 1

# Play conversion effects
execute at @s positioned ~ ~.3 ~ run particle minecraft:heart ~ ~ ~ 0.1 0.1 0.1 .001 1
execute at @s run playsound minecraft:entity.wolf.pant neutral @a[tag=!global.ignore] ~ ~ ~

# Give executing Player a dog hat
loot give @p[tag=!global.ignore,distance=..0.001] loot oran9eutan:hats/dog_hat_from_dog
execute as @s at @s run function oran9eutan:hats/utils/remove_entity_silently