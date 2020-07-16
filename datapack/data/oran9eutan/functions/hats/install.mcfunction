# Installs the datapack

# Create scoreboards
scoreboard objectives add hatsMath dummy
scoreboard objectives add hatsDrpdLthrHlmt minecraft.dropped:minecraft.leather_helmet
scoreboard objectives add hatsDrpdStick minecraft.dropped:minecraft.stick
scoreboard objectives add hats.fix_old_hat trigger

#region: Init settings

#define score_holder #opt_convert_dogs Should Players be able to convert dogs to hats and back
execute unless score #opt_convert_dogs hatsConfig matches -2147483648.. run scoreboard players set #opt_convert_dogs hatsConfig 1

#define score_holder #opt_dress_mobs Randomly dress mobs in the world with hats
execute unless score #opt_dress_mobs hatsConfig matches -2147483648.. run scoreboard players set #opt_dress_mobs hatsConfig 1

#define score_holder #opt_enable_fix_old_hats Should players be able to fix their old hats
execute unless score #opt_enable_fix_old_hats hatsConfig matches -2147483648.. run scoreboard players set #opt_enable_fix_old_hats hatsConfig 0

#endregion

# Flag datapack as installed
#define score_holder #installed_version Indicating which version is installed
scoreboard players set #installed_version hatsConfig 20300

# Install message
tellraw @a ["",{"text":"Installed ","color":"gold"},{"text":"Hats","color":"red"},{"text":" datapack version ","color":"gold"},{"score":{"name":"#installed_version","objective":"hatsConfig"},"color":"red"}]