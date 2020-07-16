# Disables Players from converting dogs into hats and back

scoreboard players set #opt_convert_dogs hats.cfg 0
schedule clear oran9eutan:hats/loops/convert_thrown_dog_hat_items

tellraw @s [{"text":"Disabled","color":"red"},{"text":" option \"Convert dogs\"","color":"gold"}]