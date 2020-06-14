# Installs the datapack

# Create scoreboards
scoreboard objectives add hatsMath dummy
scoreboard objectives add hatsDrpdLthrHlmt minecraft.dropped:minecraft.leather_helmet
scoreboard objectives add hatsDrpdStick minecraft.dropped:minecraft.stick

#region: Init settings

#define score_holder #opt_convert_dogs Option if Players can convert dogs to hats and back. Enabled if 1, disabled otherwise
execute unless score #opt_convert_dogs hatsConfig matches -2147483648.. run scoreboard players set #opt_convert_dogs hatsConfig 1

#endregion

# Flag datapack as installed
#define score_holder #installed_version Indicating which version is installed
scoreboard players set #installed_version hatsConfig 20300

# Install message
tellraw @a ["",{"text":"Installed ","color":"gold"},{"text":"Hats","color":"red"},{"text":" datapack version ","color":"gold"},{"score":{"name":"#installed_version","objective":"hatsConfig"},"color":"red"}]