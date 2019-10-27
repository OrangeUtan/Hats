###################################################
# as: Player                                      #
# Descr: Replace #hat item with #hat_on_head item #
###################################################

clear @s minecraft:stick{Tags:["is_hat"],CustomModelData:7773181} 1
execute as @s run loot give @s loot hats:hat/halloween/native_american_headband