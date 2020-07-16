execute as @a[tag=!global.ignore] if score @s hats.fix_old_hat matches 1.. run function oran9eutan:hats/fix_old_hats/fix_selected_hat

# loop
execute if score #opt_enable_fix_old_hats hats.cfg matches 1 run schedule function oran9eutan:hats/loops/did_player_triggered_fix_old_hat 5t