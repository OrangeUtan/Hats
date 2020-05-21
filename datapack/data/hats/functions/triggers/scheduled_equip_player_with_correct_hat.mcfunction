####################################################################
# as: World                                                        #
# Descr: Fix hats on players that need fixing   		           #
####################################################################

execute as @a[nbt={Inventory:[{Slot:103b,id:"minecraft:leather_helmet",tag:{Tags:["is_hat"]}}]}] run function hats:hat_behavior/equip_player_with_correct_hat