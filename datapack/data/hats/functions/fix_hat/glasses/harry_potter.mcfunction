###################################################
# as: Player                                      #
# Descr: Replace #hat item with #hat_on_head item #
###################################################

clear @s minecraft:stick{Tags:["is_hat"],CustomModelData:3141} 1
execute as @s run loot give @s loot hats:hat/glasses/harry_potter