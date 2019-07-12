# Created by Oran9eUtan

# Add posX
execute as @s store result score #hats_rand hats_register run data get entity @s Pos[0] 10000
scoreboard players operation #hats_rand hats_rand_num += #hats_rand hats_register

# Add posY
execute as @s store result score #hats_rand hats_register run data get entity @s Pos[2] 10000
scoreboard players operation #hats_rand hats_rand_num += #hats_rand hats_register

# Add posZ
execute as @s store result score #hats_rand hats_register run data get entity @s Pos[3] 10000
scoreboard players operation #hats_rand hats_rand_num += #hats_rand hats_register

# Keep the result in range
scoreboard players operation #hats_rand hats_rand_num %= #hats_rand hats_range_up