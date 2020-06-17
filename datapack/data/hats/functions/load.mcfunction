# Initialises the datapack
# executor: World

# Install datapack if it is not already
scoreboard objectives add hatsConfig dummy
execute unless score #installed_version hatsConfig matches 20301 run function hats:install

#region: Start looping functions
execute if score #opt_convert_dogs hatsConfig matches 1 run function hats:loops/convert_thrown_dog_hat_items
execute if score #opt_dress_mobs hatsConfig matches 1 run function hats:loops/dress_mobs
function hats:loops/replace_helmet_hats_on_armorstands
#endregion