#############
# as: World #
#############

#----------------------------------------------------------------------#
# Replace helmet-hats with item-hats:                                  #          
# Hats are custom helmet models, which allows them to be used as such. #
# But since helmets cannot display their a custom model on a head,     #
# the following code replaces them with an item that can               #
#----------------------------------------------------------------------#

# Replace helmet on armorstand
execute as @e[type=minecraft:armor_stand,nbt={ArmorItems:[{},{},{},{id:"minecraft:leather_helmet",tag:{Tags:["is_hat"]}}]}] run function hats:hat_behavior/equip_armorstand_with_correct_hat