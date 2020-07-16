# Enables players to fix their old hats

scoreboard players set #opt_enable_fix_old_hats hatsConfig 1
scoreboard players reset @a hats.fix_old_hat

scoreboard players enable @a hats.fix_old_hat
function oran9eutan:hats/loops/did_player_triggered_fix_old_hat

tellraw @s [{"text":"Enabled ","color":"green"},{"text":"option \"Fix old hats\"","color":"gold"}] 