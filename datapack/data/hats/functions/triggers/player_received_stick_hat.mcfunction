# executor: Player getting advancement
# descr: Called by advancement when the players inventory contains a stick hat. Replaces it with a helmet hat

execute if entity @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"]}}]}] run schedule function hats:proxies/fix_players_stick_hats_if_necessary 1t

# Reset trigger
advancement revoke @s only hats:triggers/player_received_stick_hat