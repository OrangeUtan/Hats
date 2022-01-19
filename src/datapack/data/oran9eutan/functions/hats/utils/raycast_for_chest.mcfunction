# Casts a distance limited ray that stops if it hits a chest

# Set the max distance of the ray
#define score_holder #raysteps Maximum number of steps a raycast takes
scoreboard players set #raysteps hats.math 25

# Cast the ray
execute anchored eyes run function oran9eutan:hats/utils/raycast_for_chest_rec

scoreboard players reset #raystep hats.math
