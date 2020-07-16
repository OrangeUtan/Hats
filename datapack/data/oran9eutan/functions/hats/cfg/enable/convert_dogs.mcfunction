# Enables Players to convert dogs into hats and back

scoreboard players set #opt_convert_dogs hats.cfg 1
function oran9eutan:hats/loops/convert_dogs_near_players

tellraw @s [{"text":"Enabled ","color":"green"},{"text":"option \"Convert dogs\"","color":"gold"}] 