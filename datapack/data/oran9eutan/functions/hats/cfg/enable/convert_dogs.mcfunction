# Enables Players to convert dogs into hats and back

scoreboard players set #opt_convert_dogs hats.cfg 1
function oran9eutan:hats/loops/convert_thrown_dog_hat_items

tellraw @s [{"text":"Enabled ","color":"green"},{"text":"option \"Convert dogs\"","color":"gold"}] 