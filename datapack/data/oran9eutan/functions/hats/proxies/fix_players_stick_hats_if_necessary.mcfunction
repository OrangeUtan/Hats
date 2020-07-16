# executor: World
# descr: This function is scheduled as a proxy, so that another function call can be scheduled with a desired context

# Execute proxied function as Players that received a stick hat
execute as @a[tag=!global.ignore,tag=hats.player.received_stick_hat] run function oran9eutan:hats/hat_mechanism/fix_players_stick_hats_if_necessary
tag @a remove hats.player.received_stick_hat