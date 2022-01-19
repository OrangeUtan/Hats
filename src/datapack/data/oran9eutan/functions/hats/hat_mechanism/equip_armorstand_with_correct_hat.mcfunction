########################################################################
# as: ArmorStand                                                       #
# Descr: Replace the #hat on the ArmorStands head with an #hat_on_head #
########################################################################

# Since #hat_inventory and #hat_head items have the same nbt, only change the item id
data modify entity @s ArmorItems[3] merge value {id:"{{ hats.default_item_head }}"}
