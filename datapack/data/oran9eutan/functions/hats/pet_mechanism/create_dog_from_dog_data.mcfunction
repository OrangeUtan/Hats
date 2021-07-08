# Creates a dog from stored dog_data
# @s: Nearest player from recently droped dog hat item

# Summon dog
summon minecraft:wolf ~ ~ ~ {Tags:["hats_dog_from_hat"]}


# Merge dog nbt with saved dogs nbt
execute as @e[type=wolf,distance=..0.001,tag=hats_dog_from_hat,limit=1] run function oran9eutan:hats/pet_mechanism/merge_dog_data
execute positioned ~ ~.3 ~ run particle minecraft:poof ~ ~ ~ 0.1 0.1 0.1 .001 5
playsound minecraft:entity.wolf.ambient neutral @a[tag=!global.ignore] ~ ~ ~

# Give player a lead
summon item ~ ~ ~ {PickupDelay:1,Item:{id:"minecraft:lead",Count:1b}}
