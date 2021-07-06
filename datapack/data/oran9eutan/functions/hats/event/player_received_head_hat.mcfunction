# Triggered via advancement when a players inventory contains a #hat_head.
# Replaces it with a #hat_inventory.
# @s: Player that made the advancement

# Tag Player that they received a #hat_head
tag @s add hats.tmp.received_head_hat
# Fix the #hat_head in the next tick. Changing the inventory on an advancement trigger is buggy
schedule function oran9eutan:hats/proxies/fix_players_stick_hats_if_necessary 1t

# Reset trigger
advancement revoke @s only oran9eutan:hats/event/player_received_head_hat
