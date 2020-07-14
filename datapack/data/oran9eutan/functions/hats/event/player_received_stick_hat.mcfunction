# executor: Player getting advancement
# descr: Called by advancement when the players inventory contains a stick hat. Replaces it with a helmet hat

# Tag Player that he received a stick hat
tag @s add hats.player.received_stick_hat
# Fix the stick hat in the next tick. Changing the inventory on an advancement trigger is buggy
schedule function oran9eutan:hats/proxies/fix_players_stick_hats_if_necessary 1t

# Reset trigger
advancement revoke @s only oran9eutan:hats/event/player_received_stick_hat