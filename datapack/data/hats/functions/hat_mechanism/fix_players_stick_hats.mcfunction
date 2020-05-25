# executor: Player who has a stick hat in his inventory that needs to be fixed
# descr: When a Player takes of their hat, they have #hat_on_head item in their inventory.
#        Replace that item with an equivalent #hat item

# Extract items in hotbar from buffer.all
data modify storage minecraft:hats buffer.hotbar append from storage minecraft:hats buffer.all[{Slot:0b}]
data modify storage minecraft:hats buffer.hotbar append from storage minecraft:hats buffer.all[{Slot:1b}]
data modify storage minecraft:hats buffer.hotbar append from storage minecraft:hats buffer.all[{Slot:2b}]
data modify storage minecraft:hats buffer.hotbar append from storage minecraft:hats buffer.all[{Slot:3b}]
data modify storage minecraft:hats buffer.hotbar append from storage minecraft:hats buffer.all[{Slot:4b}]
data modify storage minecraft:hats buffer.hotbar append from storage minecraft:hats buffer.all[{Slot:5b}]
data modify storage minecraft:hats buffer.hotbar append from storage minecraft:hats buffer.all[{Slot:6b}]
data modify storage minecraft:hats buffer.hotbar append from storage minecraft:hats buffer.all[{Slot:7b}]
data modify storage minecraft:hats buffer.hotbar append from storage minecraft:hats buffer.all[{Slot:8b}]

execute if data storage minecraft:hats buffer.hotbar[{id:"minecraft:stick", tag:{Tags:["is_hat"]}}] run function hats:hat_mechanism/fix_players_stick_hats_in_hotbar

# Extract items in inventory from buffer.all
data modify storage minecraft:hats buffer.inventory append from storage minecraft:hats buffer.all[{Slot:9b}]
data modify storage minecraft:hats buffer.inventory append from storage minecraft:hats buffer.all[{Slot:10b}]
data modify storage minecraft:hats buffer.inventory append from storage minecraft:hats buffer.all[{Slot:11b}]
data modify storage minecraft:hats buffer.inventory append from storage minecraft:hats buffer.all[{Slot:12b}]
data modify storage minecraft:hats buffer.inventory append from storage minecraft:hats buffer.all[{Slot:13b}]
data modify storage minecraft:hats buffer.inventory append from storage minecraft:hats buffer.all[{Slot:14b}]
data modify storage minecraft:hats buffer.inventory append from storage minecraft:hats buffer.all[{Slot:15b}]
data modify storage minecraft:hats buffer.inventory append from storage minecraft:hats buffer.all[{Slot:16b}]
data modify storage minecraft:hats buffer.inventory append from storage minecraft:hats buffer.all[{Slot:17b}]
data modify storage minecraft:hats buffer.inventory append from storage minecraft:hats buffer.all[{Slot:18b}]
data modify storage minecraft:hats buffer.inventory append from storage minecraft:hats buffer.all[{Slot:19b}]
data modify storage minecraft:hats buffer.inventory append from storage minecraft:hats buffer.all[{Slot:20b}]
data modify storage minecraft:hats buffer.inventory append from storage minecraft:hats buffer.all[{Slot:21b}]
data modify storage minecraft:hats buffer.inventory append from storage minecraft:hats buffer.all[{Slot:22b}]
data modify storage minecraft:hats buffer.inventory append from storage minecraft:hats buffer.all[{Slot:23b}]
data modify storage minecraft:hats buffer.inventory append from storage minecraft:hats buffer.all[{Slot:24b}]
data modify storage minecraft:hats buffer.inventory append from storage minecraft:hats buffer.all[{Slot:25b}]
data modify storage minecraft:hats buffer.inventory append from storage minecraft:hats buffer.all[{Slot:26b}]
data modify storage minecraft:hats buffer.inventory append from storage minecraft:hats buffer.all[{Slot:27b}]
data modify storage minecraft:hats buffer.inventory append from storage minecraft:hats buffer.all[{Slot:28b}]
data modify storage minecraft:hats buffer.inventory append from storage minecraft:hats buffer.all[{Slot:29b}]
data modify storage minecraft:hats buffer.inventory append from storage minecraft:hats buffer.all[{Slot:30b}]
data modify storage minecraft:hats buffer.inventory append from storage minecraft:hats buffer.all[{Slot:31b}]
data modify storage minecraft:hats buffer.inventory append from storage minecraft:hats buffer.all[{Slot:32b}]
data modify storage minecraft:hats buffer.inventory append from storage minecraft:hats buffer.all[{Slot:33b}]
data modify storage minecraft:hats buffer.inventory append from storage minecraft:hats buffer.all[{Slot:34b}]
data modify storage minecraft:hats buffer.inventory append from storage minecraft:hats buffer.all[{Slot:35b}]

execute if data storage minecraft:hats buffer.inventory[{id:"minecraft:stick", tag:{Tags:["is_hat"]}}] run function hats:hat_mechanism/fix_players_stick_hats_in_inventory