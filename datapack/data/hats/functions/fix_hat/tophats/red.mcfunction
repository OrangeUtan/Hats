# as: Player, descr: Replace #hat item with equivalent #hat_on_head item
clear @s minecraft:stick{CustomModelData:3114, Tags:["is_hat"]} 1
execute as @s run loot give @s loot hats:hat/tophats/red