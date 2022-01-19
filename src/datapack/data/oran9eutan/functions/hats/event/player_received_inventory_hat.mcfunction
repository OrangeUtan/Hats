# Triggered via advancement when a players inventory contains a #hat_inventory.
# If the item is on the players head, replace it with a #hat_head.
# @s: Player that made the advancement

# Check if the item is on the players hat. If so, schedule to fix it
execute if predicate oran9eutan:hats/entity/wears_inventory_hat run schedule function oran9eutan:hats/proxies/equip_player_with_correct_hat 1t

# Reset trigger
advancement revoke @s only oran9eutan:hats/event/player_received_inventory_hat
