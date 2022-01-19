# This function is scheduled as a proxy, so that another function call can be scheduled with a desired context
# @s: World

# Execute proxied function as Players that received a #hat_head hat
execute as @a[tag=!global.ignore,tag=hats.tmp.received_head_hat] run function oran9eutan:hats/hat_mechanism/fix_players_head_hats_if_necessary
tag @a remove hats.tmp.received_head_hat
