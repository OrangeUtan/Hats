# executor: Player getting advancement
# descr: Called by advancement when the players inventory contains a helmet hat. 
#        If the hat is on the players head, replace it with a stick hat

# Check if the hat is on the players hat. If so, schedule to fix it
execute if entity @s[nbt={Inventory:[{Slot:103b,id:"minecraft:leather_helmet",tag:{Tags:["hats.hat"]}}]}] run schedule function hats:proxies/equip_player_with_correct_hat 1t

# Reset trigger
advancement revoke @s only hats:triggers/player_received_helmet_hat