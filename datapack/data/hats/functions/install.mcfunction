# Installs the datapack

# Create scoreboards
scoreboard objectives add hatsMath dummy
scoreboard objectives add hatsDrpdLthrHlmt minecraft.dropped:minecraft.leather_helmet
scoreboard objectives add hatsDrpdStick minecraft.dropped:minecraft.stick

# Flag datapack as installed
#define score_holder #installed_version Indicating which version is installed
scoreboard players set #installed_version hatsConfig 20300

# Install message
tellraw @a ["",{"text":"Installed ","color":"gold"},{"text":"Hats","color":"red"},{"text":" datapack version ","color":"gold"},{"score":{"name":"#installed_version","objective":"hatsConfig"},"color":"red"}]