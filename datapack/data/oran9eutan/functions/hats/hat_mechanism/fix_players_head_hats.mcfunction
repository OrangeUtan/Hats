# Replaces any #hat_head hats in the players inventory with #hat_inventory hats
# @s: Player who has a #hat_head hat in their inventory

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

execute if data storage minecraft:hats buffer.hotbar[{id:"{{ hats.default_item_head }}", tag:{Tags:["hats.hat"]}}] run function oran9eutan:hats/hat_mechanism/fix_players_head_hats_in_hotbar

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
execute if data storage minecraft:hats buffer.inv[{id:"{{ hats.default_item_head }}", tag:{Tags:["hats.hat"]}}] run function oran9eutan:hats/hat_mechanism/fix_players_head_hats_in_inventory
