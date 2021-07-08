# Player dropped a #hat_head or a #hat_inventory. Not certain that item is a hat
# @s: Player that made advancement

# Convert all nearby dog hat items into dogs
execute if {{ hats.setting["pet_conversion"].is_true }} as @e[type=item,distance=..2,nbt={Item:{tag:{Tags:["hats.hat.type.dog"]}}}] at @s if data entity @s Item.tag.dog_data run function oran9eutan:hats/pet_mechanism/copy_dog_data_from_item

# Reset trigger
scoreboard players set @s hats.dropLthrHlm 0
scoreboard players set @s hats.drpWFOAS 0
advancement revoke @s only oran9eutan:hats/event/player_dropped_hat_item
