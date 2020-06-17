# Disables randomly dressing mobs with hats

scoreboard players set #opt_dress_mobs hatsConfig 0
schedule clear hats:loops/dress_mobs

tellraw @s [{"text":"Disabled","color":"red"},{"text":" option \"Dress mobs\"","color":"gold"}]