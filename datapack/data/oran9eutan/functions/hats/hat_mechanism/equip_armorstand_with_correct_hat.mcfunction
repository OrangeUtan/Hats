########################################################################
# as: ArmorStand                                                       #
# Descr: Replace the #hat on the ArmorStands head with an #hat_on_head #   
########################################################################

# Since #hat and #hat_on_head items have the same nbt, only change the item id
data modify entity @s ArmorItems[3] merge value {id:"minecraft:stick"}