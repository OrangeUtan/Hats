###################################################
# as: Player                                      #
# Descr: Replace #hat item with #hat_on_head item #
###################################################

clear @s minecraft:stick{Tags:["is_hat"],CustomModelData:3154} 1
execute as @s run loot give @s loot hats:hat/accessories/snorkel_mask_red