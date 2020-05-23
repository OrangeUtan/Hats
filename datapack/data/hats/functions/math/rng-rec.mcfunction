# Calculate next lcg value
function hats:math/lcg

# Store current lcg value in 'rand_num' and 'tmp'
scoreboard players operation #hats_rand_num hats_math = #hats_lcg hats_math
scoreboard players operation #hats_tmp hats_math = #hats_lcg hats_math

# Calculate random number inside range
scoreboard players operation #hats_rand_num hats_math %= #hats_rng_range hats_math
scoreboard players operation #hats_tmp hats_math -= #hats_rand_num hats_math
scoreboard players operation #hats_tmp hats_math += #hats_m hats_math

# Loop if value is negative
execute if score #hats_tmp hats_math matches ..-1 run function hats:math/lcg_next