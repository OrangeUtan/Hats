# Player dropped a #hat_head or a #hat_inventory. Not certain that item is a hat
# @s: Player that made advancement

execute if {{ hats.setting["pet_conversion"].is_true }} as @e[type=item,distance=..2,limit=1,predicate=oran9eutan:hats/entity/item_is_pet_hat] run function oran9eutan:hats/pet_mechanism/convert_hat_to_pet

# Reset trigger
scoreboard players set @s hats.dropLthrHlm 0
scoreboard players set @s hats.drpWFOAS 0
advancement revoke @s only oran9eutan:hats/event/player_dropped_hat_item
