# Converts a dog hat into a dog
# @s: Dog hat item beeing converted to a dog

# Move the saved dogs nbt into storage
data modify storage hats dog_data set from entity @s Item.tag.dog_data
data modify storage hats dog_data.CustomName set from entity @s Item.tag.display.Name

# Create dog at players position
execute as @p[tag=!global.ignore] at @s run function oran9eutan:hats/dog_mechanism/create_dog_from_dog_data

# Remove temporary storage
data remove storage hats dog_data

kill @s
