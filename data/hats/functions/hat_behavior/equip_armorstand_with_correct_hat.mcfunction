# Created by Oran9eUtan

#------------------------------------------------#
# Replace helmet-hat on armorstand with item-hat #
#------------------------------------------------#

# --- Since helmet-hats and stick-hats have the same nbt, only change the item id ---
data modify entity @s ArmorItems[3] merge value {id:"minecraft:stick",tag:{Tags:["hat_on_armorstand","is_hat"]}}