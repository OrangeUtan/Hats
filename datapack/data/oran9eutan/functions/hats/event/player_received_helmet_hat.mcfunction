# executor: Player getting advancement
# descr: Called by advancement when the players inventory contains a helmet hat. 
#        If the hat is on the players head, replace it with a stick hat

# Check if the hat is on the players hat. If so, schedule to fix it
execute if predicate oran9eutan:hats/entity/wears_leather_helmet_hat run schedule function oran9eutan:hats/proxies/equip_player_with_correct_hat 1t

# Reset trigger
advancement revoke @s only oran9eutan:hats/event/player_received_helmet_hat