####################################################################
# as: Player getting advancement                                   #
# Descr: Called by advancement when the players inventory          #
#        contains a hat. If the hat is on the players head,        #
#        replace it with a HOH-hat 						           #
####################################################################

# Check if the hat is on the players hat. If so, schedule to fix it
execute if entity @s[nbt={Inventory:[{Slot:103b,id:"minecraft:leather_helmet",tag:{Tags:["is_hat"]}}]}] run schedule function hats:triggers/scheduled_equip_player_with_correct_hat 1t

# Reset trigger
advancement revoke @s only hats:triggers/player_received_helmet_hat