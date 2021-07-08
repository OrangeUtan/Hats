# Creates a pet from pet_data in storage
# @s: Nearest player to the recently dropped pet hat item

# Summon pet
summon minecraft:wolf ~ ~ ~ {Tags:["hats.entity.pet_from_hat"]}

# Merge the pets nbt with the stored pet_data
execute as @e[type=wolf,distance=..0.001,tag=hats.entity.pet_from_hat,limit=1] run function oran9eutan:hats/pet_mechanism/merge_pet_with_stored_data

# Effects
playsound minecraft:entity.wolf.ambient neutral @a[tag=!global.ignore] ~ ~ ~
execute positioned ~ ~.3 ~ run particle minecraft:poof ~ ~ ~ 0.1 0.1 0.1 .001 5

# Return lead to player
summon item ~ ~ ~ {PickupDelay:1,Item:{id:"minecraft:lead",Count:1b}}
