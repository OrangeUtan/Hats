# Enables randomly dressing mobs with hats 

scoreboard players set #opt_dress_mobs hats.cfg 1
function oran9eutan:hats/loops/dress_mobs

tellraw @s [{"text":"Enabled ","color":"green"},{"text":"option \"Dress mobs\"","color":"gold"}] 