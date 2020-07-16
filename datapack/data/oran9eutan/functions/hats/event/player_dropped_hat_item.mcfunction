# Player dropped a stick or a leather helmet. Not certain that item is a hat
# executor: Player getting advancement

# Convert all nearby dog hat items into dogs
execute if score #opt_convert_dogs hats.cfg matches 1 as @e[type=item,distance=..2,nbt={Item:{tag:{Tags:["hats.hat.type.dog"]}}}] at @s if data entity @s Item.tag.dog_data run function oran9eutan:hats/dog_mechanism/create_dog_from_hat_item

# Reset trigger
scoreboard players set @s hatsDrpdLthrHlmt 0
scoreboard players set @s hatsDrpdStick 0
advancement revoke @s only oran9eutan:hats/event/player_dropped_hat_item