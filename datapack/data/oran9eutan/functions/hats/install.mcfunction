
# Add scoreboards
scoreboard objectives add hats.cfg dummy
scoreboard objectives add hats.math dummy
scoreboard objectives add hats.dropLthrHlm minecraft.dropped:minecraft.leather_helmet
scoreboard objectives add hats.dropWFOAS minecraft.dropped:minecraft.warped_fungus_on_a_stick

# Init configuration
function oran9eutan:hats/cfg/init

# Flag datapack as installed
data modify storage oran9eutan.hats version set value {"major": 2, "minor": 3, "patch": 1}
