# Merges the nbt of a pet with the stored pet_data
# @s: Pet whose nbt is beeing modified

data modify entity @s CollarColor set from storage minecraft:hats pet_data.CollarColor
data modify entity @s Age set from storage minecraft:hats pet_data.Age
data modify entity @s ForcedAge set from storage minecraft:hats pet_data.ForcedAge
data modify entity @s Attributes set from storage minecraft:hats pet_data.Attributes
data modify entity @s Invulnerable set from storage minecraft:hats pet_data.Invulnerable
data modify entity @s CustomName set from storage minecraft:hats pet_data.CustomName
data modify entity @s CustomNameVisible set from storage minecraft:hats pet_data.CustomNameVisible
data modify entity @s Tags set from storage minecraft:hats pet_data.Tags
data modify entity @s Owner set from storage minecraft:hats pet_data.Owner

tag @s remove hats.entity.pet_from_hat
