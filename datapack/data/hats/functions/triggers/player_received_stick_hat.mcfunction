# Check if the hat is on the players hat. If so, schedule to fix it
execute if entity @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"]}}]}] run schedule function hats:scheduled_proxies/fix_stick_hats_in_players_inventory 1t

# Reset trigger
advancement revoke @s only hats:triggers/player_received_stick_hat