# descr: Calculates a random number. 
#        Lower (inclusive) bound is 0, upper (exclusive) bound is score 'hats_math' of player '#hats_rng_range'

# m = range - 1
scoreboard players operation #hats_m hats_math = #hats_rng_range hats_math
scoreboard players remove #hats_m hats_math 1

# Calculate random number inside range
function hats:math/rng-rec