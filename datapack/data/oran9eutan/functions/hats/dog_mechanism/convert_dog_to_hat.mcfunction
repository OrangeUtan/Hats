# Converts a dog into a dog hat and stores its data in the hat
# executor: Dog beeing converted to a hat

# Give executing Player a dog hat
loot give @p[distance=..0.001] loot oran9eutan:hats/dog_hat_from_dog
execute as @s at @s run function oran9eutan:hats/utils/remove_entity_silently