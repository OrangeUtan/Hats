########################################
# as: World                            #
# Descr: Initialises the Hats datapack #
########################################

#-----------------#
# Add Scoreboards #
#-----------------#

scoreboard objectives add hats_min_price dummy
scoreboard objectives add hats_max_price dummy
scoreboard objectives add hats_math dummy

# Initialise random number generator
function hats:math/lcg_init

#---------------------------------------#
# Start repeating 'dress_mobs' function #
#---------------------------------------#

# Dresses new mobs with hats every x seconds 
function hats:dress/dress_mobs_with_hats

#----------------------#
# Start tick functions #
#----------------------#
function hats:every_3t
function hats:every_5s
function hats:every_60s