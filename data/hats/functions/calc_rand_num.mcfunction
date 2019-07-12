# Created by Oran9eUtan


# UUIDMost and UUIDLeast are 64 bit Longs, but Scoreboards only can save 32 bit values.
# To get the first 32 bits of each UUID part, scale them by 1/(2^31-1) ~= 0.00000000023...
# 0.0000000001 is close enough and gives better results

# Store the first ~32 bits of UUIDMost.
# The UUID insures, that even if all other parameters are the same for 2 mobs, its nearly impossible for them to generate the same random number
execute as @s store result score @s hats_rand_num run data get entity @s UUIDMost 0.0000000001

# Add posX
execute as @s store result score @s hats_register run data get entity @s Pos[0] 10000
scoreboard players operation @s hats_rand_num += @s hats_register

# Add posY
execute as @s store result score @s hats_register run data get entity @s Pos[2] 10000
scoreboard players operation @s hats_rand_num += @s hats_register

# Add posZ
execute as @s store result score @s hats_register run data get entity @s Pos[3] 10000
scoreboard players operation @s hats_rand_num += @s hats_register

# Keep the result in range
scoreboard players operation @s hats_rand_num %= @s hats_range_up