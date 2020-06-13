# Initialises the datapack
# executor: World

# Scoreboards
scoreboard objectives add hatsConfig dummy
scoreboard objectives add hatsMath dummy
scoreboard objectives add hatsDrpdLthrHlmt minecraft.dropped:minecraft.leather_helmet
scoreboard objectives add hatsDrpdStick minecraft.dropped:minecraft.stick

# Start tick functions
function hats:every_3t
function hats:every_5s
function hats:every_60s

#region: Start looping functions
#define score_holder #opt_convert_dogs Option if Players can convert dogs to hats and back. Enabled if 1, disabled otherwise
execute if score #opt_convert_dogs hatsConfig matches 1 run function hats:loops/convert_thrown_dog_hat_items

#endregion