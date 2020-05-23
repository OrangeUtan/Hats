# Linear congruential generator (Random number generator). Calculates a pseudo-random number.
# Formula: x_{n+1} = x_n * 1103515245 + 12345

scoreboard players operation #hats_lcg hats_math *= #hats_lcg_mult hats_math
scoreboard players add #hats_lcg hats_math 12345