# executor: Player whos inventory is getting fixed
# descr: Fixes all stick hats in the Players inventory slots
# requirements: 
# 	- storage buffer.inventory has to be populated
#   - at least one stick hat has to exist in buffer.inventory

# Correct slot data
data modify storage minecraft:hats buffer.inventory[{Slot:9b}].Slot set value 0b
data modify storage minecraft:hats buffer.inventory[{Slot:10b}].Slot set value 1b
data modify storage minecraft:hats buffer.inventory[{Slot:11b}].Slot set value 2b
data modify storage minecraft:hats buffer.inventory[{Slot:12b}].Slot set value 3b
data modify storage minecraft:hats buffer.inventory[{Slot:13b}].Slot set value 4b
data modify storage minecraft:hats buffer.inventory[{Slot:14b}].Slot set value 5b
data modify storage minecraft:hats buffer.inventory[{Slot:15b}].Slot set value 6b
data modify storage minecraft:hats buffer.inventory[{Slot:16b}].Slot set value 7b
data modify storage minecraft:hats buffer.inventory[{Slot:17b}].Slot set value 8b
data modify storage minecraft:hats buffer.inventory[{Slot:18b}].Slot set value 9b
data modify storage minecraft:hats buffer.inventory[{Slot:19b}].Slot set value 10b
data modify storage minecraft:hats buffer.inventory[{Slot:20b}].Slot set value 11b
data modify storage minecraft:hats buffer.inventory[{Slot:21b}].Slot set value 12b
data modify storage minecraft:hats buffer.inventory[{Slot:22b}].Slot set value 13b
data modify storage minecraft:hats buffer.inventory[{Slot:23b}].Slot set value 14b
data modify storage minecraft:hats buffer.inventory[{Slot:24b}].Slot set value 15b
data modify storage minecraft:hats buffer.inventory[{Slot:25b}].Slot set value 16b
data modify storage minecraft:hats buffer.inventory[{Slot:26b}].Slot set value 17b
data modify storage minecraft:hats buffer.inventory[{Slot:27b}].Slot set value 18b
data modify storage minecraft:hats buffer.inventory[{Slot:28b}].Slot set value 19b
data modify storage minecraft:hats buffer.inventory[{Slot:29b}].Slot set value 20b
data modify storage minecraft:hats buffer.inventory[{Slot:30b}].Slot set value 21b
data modify storage minecraft:hats buffer.inventory[{Slot:31b}].Slot set value 22b
data modify storage minecraft:hats buffer.inventory[{Slot:32b}].Slot set value 23b
data modify storage minecraft:hats buffer.inventory[{Slot:33b}].Slot set value 24b
data modify storage minecraft:hats buffer.inventory[{Slot:34b}].Slot set value 25b
data modify storage minecraft:hats buffer.inventory[{Slot:35b}].Slot set value 26b

# Replace all stick Hats with helmet hats
data modify storage minecraft:hats buffer.inventory[{id:"minecraft:stick", tag:{Tags:["is_hat"]}}].id set value "minecraft:leather_helmet"

# Replaced Players inventory with modified inventory
setblock ~ 0 ~ minecraft:yellow_shulker_box
data modify block ~ 0 ~ Items set from storage minecraft:hats buffer.inventory
loot replace entity @s inventory.0 27 mine ~ 0 ~ minecraft:diamond_pickaxe{drop_contents:1b}

# Clean up
setblock ~ 0 ~ minecraft:air