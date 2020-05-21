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

#----------------------------------------------------------------------------------#
# Fix Hats in Players Inventory:                                                   #
# Hats are items while they are on an entities head.                               # 
# Thats why, when a player gets his hands on one of these                          #
# (taking hat off, taking one from an armostand, ...), they can't put it on again. #
# To fix this, replace the item-hat with a helmet-hat                              #
#----------------------------------------------------------------------------------#

# Replace worn hats (#hat_on_head) with equivalent #hat item
execute as @a[nbt=!{Inventory:[{Slot:103b,id:"minecraft:stick",tag:{Tags:["is_hat"]}}]}, nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"]}}]}] run function hats:hat_behavior/fix_hat_from_head