# executor: Player who have a stick hat in their inventory that needs to be fixed
# descr: Replaces any stick hats in the Players inventory with leather helmet hats

# Extract hotbar from buffer.inv
data modify storage minecraft:hats buffer.hotbar append from storage minecraft:hats buffer.inv[{Slot:0b}]
data modify storage minecraft:hats buffer.hotbar append from storage minecraft:hats buffer.inv[{Slot:1b}]
data modify storage minecraft:hats buffer.hotbar append from storage minecraft:hats buffer.inv[{Slot:2b}]
data modify storage minecraft:hats buffer.hotbar append from storage minecraft:hats buffer.inv[{Slot:3b}]
data modify storage minecraft:hats buffer.hotbar append from storage minecraft:hats buffer.inv[{Slot:4b}]
data modify storage minecraft:hats buffer.hotbar append from storage minecraft:hats buffer.inv[{Slot:5b}]
data modify storage minecraft:hats buffer.hotbar append from storage minecraft:hats buffer.inv[{Slot:6b}]
data modify storage minecraft:hats buffer.hotbar append from storage minecraft:hats buffer.inv[{Slot:7b}]
data modify storage minecraft:hats buffer.hotbar append from storage minecraft:hats buffer.inv[{Slot:8b}]

execute if data storage minecraft:hats buffer.hotbar[{id:"minecraft:stick", tag:{Tags:["is_hat"]}}] run function hats:hat_mechanism/fix_players_stick_hats_in_hotbar

# Remove item in offhand from buffer.inv
data remove storage minecraft:hats buffer.inv[{Slot:-106b}]

# Remove equiped armor from buffer.inv. Head slot was already removed
data remove storage minecraft:hats buffer.inv[{Slot:100b}]
data remove storage minecraft:hats buffer.inv[{Slot:101b}]
data remove storage minecraft:hats buffer.inv[{Slot:102b}]

# Remove hotbar items from buffer.inv
data remove storage minecraft:hats buffer.inv[{Slot:8b}]
data remove storage minecraft:hats buffer.inv[{Slot:7b}]
data remove storage minecraft:hats buffer.inv[{Slot:6b}]
data remove storage minecraft:hats buffer.inv[{Slot:5b}]
data remove storage minecraft:hats buffer.inv[{Slot:4b}]
data remove storage minecraft:hats buffer.inv[{Slot:3b}]
data remove storage minecraft:hats buffer.inv[{Slot:2b}]
data remove storage minecraft:hats buffer.inv[{Slot:1b}]
data remove storage minecraft:hats buffer.inv[{Slot:0b}]

# Now only items in the Players inventory should be left in buffer.inv
execute if data storage minecraft:hats buffer.inv[{id:"minecraft:stick", tag:{Tags:["is_hat"]}}] run function hats:hat_mechanism/fix_players_stick_hats_in_inventory