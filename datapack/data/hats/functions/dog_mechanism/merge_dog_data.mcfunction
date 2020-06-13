# Merges the nbt of a dog with the dog_data in storage
# executor: Dog whose nbt to modify

data modify entity @s CollarColor set from storage minecraft:hats dog_data.CollarColor
data modify entity @s Age set from storage minecraft:hats dog_data.Age
data modify entity @s ForcedAge set from storage minecraft:hats dog_data.ForcedAge
data modify entity @s Attributes set from storage minecraft:hats dog_data.Attributes
data modify entity @s Invulnerable set from storage minecraft:hats dog_data.Invulnerable
data modify entity @s CustomName set from storage minecraft:hats dog_data.CustomName
data modify entity @s CustomNameVisible set from storage minecraft:hats dog_data.CustomNameVisible
data modify entity @s Tags set from storage minecraft:hats dog_data.Tags
data modify entity @s Owner set from storage minecraft:hats dog_data.Owner

tag @s remove hats_dog_from_hat