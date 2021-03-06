# Fixes all #hat_head hats in a players inventory slots
# @s: Player whos inventory is getting fixed
# requirements:
# 	- storage buffer.inv has to be populated
#   - at least one #hat_head hat has to exist in buffer.inv

# Correct slot data
data modify storage minecraft:hats buffer.inv[{Slot:9b}].Slot set value 0b
data modify storage minecraft:hats buffer.inv[{Slot:10b}].Slot set value 1b
data modify storage minecraft:hats buffer.inv[{Slot:11b}].Slot set value 2b
data modify storage minecraft:hats buffer.inv[{Slot:12b}].Slot set value 3b
data modify storage minecraft:hats buffer.inv[{Slot:13b}].Slot set value 4b
data modify storage minecraft:hats buffer.inv[{Slot:14b}].Slot set value 5b
data modify storage minecraft:hats buffer.inv[{Slot:15b}].Slot set value 6b
data modify storage minecraft:hats buffer.inv[{Slot:16b}].Slot set value 7b
data modify storage minecraft:hats buffer.inv[{Slot:17b}].Slot set value 8b
data modify storage minecraft:hats buffer.inv[{Slot:18b}].Slot set value 9b
data modify storage minecraft:hats buffer.inv[{Slot:19b}].Slot set value 10b
data modify storage minecraft:hats buffer.inv[{Slot:20b}].Slot set value 11b
data modify storage minecraft:hats buffer.inv[{Slot:21b}].Slot set value 12b
data modify storage minecraft:hats buffer.inv[{Slot:22b}].Slot set value 13b
data modify storage minecraft:hats buffer.inv[{Slot:23b}].Slot set value 14b
data modify storage minecraft:hats buffer.inv[{Slot:24b}].Slot set value 15b
data modify storage minecraft:hats buffer.inv[{Slot:25b}].Slot set value 16b
data modify storage minecraft:hats buffer.inv[{Slot:26b}].Slot set value 17b
data modify storage minecraft:hats buffer.inv[{Slot:27b}].Slot set value 18b
data modify storage minecraft:hats buffer.inv[{Slot:28b}].Slot set value 19b
data modify storage minecraft:hats buffer.inv[{Slot:29b}].Slot set value 20b
data modify storage minecraft:hats buffer.inv[{Slot:30b}].Slot set value 21b
data modify storage minecraft:hats buffer.inv[{Slot:31b}].Slot set value 22b
data modify storage minecraft:hats buffer.inv[{Slot:32b}].Slot set value 23b
data modify storage minecraft:hats buffer.inv[{Slot:33b}].Slot set value 24b
data modify storage minecraft:hats buffer.inv[{Slot:34b}].Slot set value 25b
data modify storage minecraft:hats buffer.inv[{Slot:35b}].Slot set value 26b

# Replace all #hat_head hats with #hat_inventory hats
data modify storage minecraft:hats buffer.inv[{id:"{{ hats.default_item_head }}", tag:{Tags:["hats.hat"]}}].id set value "{{ hats.default_item_inventory }}"

# Replaced players inventory with modified inventory
setblock ~ 0 ~ minecraft:yellow_shulker_box
data modify block ~ 0 ~ Items set from storage minecraft:hats buffer.inv
loot replace entity @s inventory.0 27 mine ~ 0 ~ minecraft:air{drop_contents:1b}

# Clean up
setblock ~ 0 ~ minecraft:air
