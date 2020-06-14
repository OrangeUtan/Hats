# Initialises the datapack
# executor: World

# Install datapack if it is not already
scoreboard objectives add hatsConfig dummy
execute unless score #installed_version hatsConfig matches 20300 run function hats:install

# Start tick functions
function hats:every_3t
function hats:every_5s
function hats:every_60s

#region: Start looping functions
#define score_holder #opt_convert_dogs Option if Players can convert dogs to hats and back. Enabled if 1, disabled otherwise
execute if score #opt_convert_dogs hatsConfig matches 1 run function hats:loops/convert_thrown_dog_hat_items

#endregion