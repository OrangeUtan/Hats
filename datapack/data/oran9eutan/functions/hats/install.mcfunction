# Installs the datapack

# Create scoreboards
scoreboard objectives add hats.math dummy
scoreboard objectives add hats.dropLthrHlm minecraft.dropped:minecraft.leather_helmet
scoreboard objectives add hats.dropStick minecraft.dropped:minecraft.stick
scoreboard objectives add hats.fix_old_hat trigger

#region: Init settings

#define score_holder #opt_convert_dogs Should Players be able to convert dogs to hats and back
execute unless score #opt_convert_dogs hats.cfg matches -2147483648.. run scoreboard players set #opt_convert_dogs hats.cfg 1

#define score_holder #opt_dress_mobs Randomly dress mobs in the world with hats
execute unless score #opt_dress_mobs hats.cfg matches -2147483648.. run scoreboard players set #opt_dress_mobs hats.cfg 1

#define score_holder #opt_enable_fix_old_hats Should players be able to fix their old hats
execute unless score #opt_enable_fix_old_hats hats.cfg matches -2147483648.. run scoreboard players set #opt_enable_fix_old_hats hats.cfg 0

#endregion

# Flag datapack as installed
#define score_holder #installed_version Indicating which version is installed
scoreboard players set #installed_version hats.cfg 20300