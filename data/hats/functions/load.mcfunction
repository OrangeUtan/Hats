#################################
# Initialises the Hats datapack #
#################################

#-----------------#
# Add Scoreboards #
#-----------------#

# Used for random price
scoreboard objectives add hats_min_price dummy
scoreboard objectives add hats_max_price dummy

#-------------------------------------#
# Start repeating dress_mobs function #
#-------------------------------------#

# Dresses new mobs with hats every x seconds 
function hats:dress_mobs/dress_mobs_with_hats