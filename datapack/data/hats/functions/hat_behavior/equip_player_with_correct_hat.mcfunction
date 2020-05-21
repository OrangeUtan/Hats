####################################################################
# as: Player                                                       #
# Descr: Replace the #hat on the Players head with an #hat_on_head #
####################################################################

# Get hat
data modify storage hats buffer.all set from entity @s Inventory
data modify storage minecraft:hats buffer.armor set value []
data modify storage minecraft:hats buffer.armor append from storage minecraft:hats buffer.all[{Slot:103b}]

# Modify hat
data modify storage minecraft:hats buffer.armor[0].id set value "minecraft:stick"
data modify storage minecraft:hats buffer.armor[0].Slot set value 0b

# Replace Player helmet with modified hat
setblock ~ 255 ~20 minecraft:yellow_shulker_box
data modify block ~ 255 ~20 Items set from storage minecraft:hats buffer.armor
loot replace entity @s armor.head 1 mine ~ 255 ~20 minecraft:diamond_pickaxe{drop_contents:1b}

# Clean up
setblock ~ 255 ~20 minecraft:air
data remove storage minecraft:hats buffer