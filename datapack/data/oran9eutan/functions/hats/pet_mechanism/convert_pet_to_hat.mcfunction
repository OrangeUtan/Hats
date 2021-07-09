# Converts a pet into a hat and stores its data in the hat
# @s: Pet beeing converted to a hat

# Remove 1 lead from the players inventory
clear @p[tag=!global.ignore,distance=..0.001] lead 1

# Save the name of the owner if it isn't already
execute as @s[tag=!OwnerName] run function oran9eutan:hats/pet_mechanism/save_owner_name_on_pet

# Play conversion effects
execute at @s positioned ~ ~.3 ~ run particle minecraft:heart ~ ~ ~ 0.1 0.1 0.1 .001 1
execute if entity @s[type=wolf] at @s run playsound minecraft:entity.wolf.pant neutral @a[tag=!global.ignore] ~ ~ ~
execute if entity @s[type=cat] at @s run playsound minecraft:entity.cat.purreow neutral @a[tag=!global.ignore] ~ ~ ~

# Give player a pet hat
execute if entity @s[type=wolf] run loot give @p[tag=!global.ignore,distance=..0.001] loot oran9eutan:hats/hat_from/dog
execute if entity @s[type=cat] run loot give @p[tag=!global.ignore,distance=..0.001] loot oran9eutan:hats/hat_from/cat

# Bye bye fren :'(
execute at @s run function oran9eutan:hats/utils/remove_entity_silently
