# Installs the datapack

# Create scoreboards
scoreboard objectives add hats.math dummy
scoreboard objectives add hats.dropLthrHlm minecraft.dropped:minecraft.leather_helmet
scoreboard objectives add hats.drpWFOAS minecraft.dropped:minecraft.warped_fungus_on_a_stick
scoreboard objectives add hats.fix_old_hat trigger

# Initialize settings
function oran9eutan:hats/cfg/init

# Flag datapack as installed
data modify storage oran9eutan.hats version set value {"major": 2, "minor": 3, "patch": 1}
