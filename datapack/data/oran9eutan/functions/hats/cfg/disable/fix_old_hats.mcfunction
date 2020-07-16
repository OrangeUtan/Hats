# Disables option to allow players to fix their old hats

scoreboard players set #opt_enable_fix_old_hats hatsConfig 0
scoreboard players reset @a hats.fix_old_hat

scoreboard players reset @a hats.fix_old_hat
schedule clear oran9eutan:hats/loops/did_player_triggered_fix_old_hat

tellraw @s [{"text":"Disabled","color":"red"},{"text":" option \"Fix old hats\"","color":"gold"}]