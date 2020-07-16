# Disables randomly dressing mobs with hats

scoreboard players set #opt_dress_mobs hats.cfg 0
schedule clear oran9eutan:hats/loops/dress_mobs

tellraw @s [{"text":"Disabled","color":"red"},{"text":" option \"Dress mobs\"","color":"gold"}]