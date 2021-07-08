# Converts a hat into a pet
# @s: Hat item beeing converted to a pet

# Copy pet_data from the item to storage
data modify storage hats pet_data set from entity @s Item.tag.pet_data
data modify storage hats pet_data.CustomName set from entity @s Item.tag.display.Name

# Create pet from pet_data
execute if entity @s[predicate=oran9eutan:hats/entity/is_hat_type_dog] as @p[tag=!global.ignore] at @s run function oran9eutan:hats/pet_mechanism/create_dog_from_pet_data

# Remove temporary storage
data remove storage hats pet_data

kill @s
