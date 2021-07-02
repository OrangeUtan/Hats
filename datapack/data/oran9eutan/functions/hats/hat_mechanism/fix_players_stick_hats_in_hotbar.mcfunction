# executor: Player whos inventory is getting fixed
# descr: Fixes all stick hats in the Players hotbar slots
# requirements:
# 	- storage buffer.hotbar has to be populated
#   - at least one stick hat has to exist in buffer.hotbar

# Replace all stick hats with helmet hats
data modify storage minecraft:hats buffer.hotbar[{id:"minecraft:stick", tag:{Tags:["hats.hat"]}}].id set value "minecraft:leather_helmet"

# Replaced Players hotbar with modified hotbar
setblock ~ 0 ~ minecraft:yellow_shulker_box
data modify block ~ 0 ~ Items set from storage minecraft:hats buffer.hotbar
loot replace entity @s hotbar.0 9 mine ~ 0 ~ minecraft:air{drop_contents:1b}

# Clean up
setblock ~ 0 ~ minecraft:air
