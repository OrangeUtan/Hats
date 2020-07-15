# Converts a dog hat into a dog
# executor: Dog hat item beeing converted to a dog

# Move the saved dogs nbt into storage
data modify storage hats dog_data set from entity @s Item.tag.dog_data
data modify storage hats dog_data.CustomName set from entity @s Item.tag.display.Name

# Summon dog
summon minecraft:wolf ~ ~ ~ {Tags:["hats_dog_from_hat"]}

# Merge dog nbt with saved dogs nbt
execute as @e[type=wolf,distance=..0.001,tag=hats_dog_from_hat,limit=1] run function oran9eutan:hats/dog_mechanism/merge_dog_data

# Remove temporary storage
data remove storage hats dog_data

kill @s