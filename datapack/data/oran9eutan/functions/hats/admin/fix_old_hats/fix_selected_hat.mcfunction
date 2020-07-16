# executor: Player who triggered the command and whose selected hat will be fixed

execute store result score @s hatsMath run data get entity @s SelectedItem.tag.CustomModelData
data modify storage hats hat_to_fix set from entity @s SelectedItem

# Fix name and lore of hat
function oran9eutan:hats/admin/fix_old_hats/tree/tree-3000-7773191

# Fix custom model data of hat
execute if score @s hatsMath matches 3000 run scoreboard players set @s hatsMath 7773118
execute if score @s hatsMath matches 3001 run scoreboard players set @s hatsMath 7773119
execute if score @s hatsMath matches 3002 run scoreboard players set @s hatsMath 7773132
execute if score @s hatsMath matches 3003 run scoreboard players set @s hatsMath 7773133
execute unless score @s hatsMath matches 7770000.. run scoreboard players add @s hatsMath 7770000
execute store result storage minecraft:hats hat_to_fix.tag.CustomModelData int 1 run scoreboard players get @s hatsMath

# Replaced Players hotbar with modified hotbar
setblock ~ 0 ~ minecraft:yellow_shulker_box
data modify block ~ 0 ~ Items append from storage minecraft:hats hat_to_fix
loot replace entity @s weapon.mainhand mine ~ 0 ~ minecraft:diamond_pickaxe{drop_contents:1b}

# Clean up
setblock ~ 0 ~ minecraft:air

# Allow player to fix more hats
scoreboard players set @s hats.fix_old_hat 0
execute if score #opt_enable_fix_old_hats hatsConfig matches 1 run scoreboard players enable @s hats.fix_old_hat