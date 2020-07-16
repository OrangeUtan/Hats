# Initialises the datapack
# executor: World

# Install datapack if it is not already
scoreboard objectives add hats.cfg dummy
execute unless score #installed_version hats.cfg matches 20300 run function oran9eutan:hats/install

#Start looping functions
execute if score #opt_convert_dogs hats.cfg matches 1 run function oran9eutan:hats/loops/convert_dogs_near_players
execute if score #opt_dress_mobs hats.cfg matches 1 run function oran9eutan:hats/loops/dress_mobs
execute if score #opt_enable_fix_old_hats hats.cfg matches 1 run function oran9eutan:hats/loops/did_player_triggered_fix_old_hat