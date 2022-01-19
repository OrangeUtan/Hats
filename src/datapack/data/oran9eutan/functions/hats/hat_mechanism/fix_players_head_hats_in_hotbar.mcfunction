# Fixes all #hat_head hats in a players hotbar slots
# @s: Player whos inventory is getting fixed
# requirements:
# 	- storage buffer.hotbar has to be populated
#   - at least one #hat_head hat has to exist in buffer.hotbar

# Replace all #hat_head hats with helmet hats
data modify storage minecraft:hats buffer.hotbar[{id:"{{ hats.default_item_head }}", tag:{Tags:["hats.hat"]}}].id set value "{{ hats.default_item_inventory }}"

# Replaced Players hotbar with modified hotbar
setblock ~ 0 ~ minecraft:yellow_shulker_box
data modify block ~ 0 ~ Items set from storage minecraft:hats buffer.hotbar
loot replace entity @s hotbar.0 9 mine ~ 0 ~ minecraft:air{drop_contents:1b}

# Clean up
setblock ~ 0 ~ minecraft:air
