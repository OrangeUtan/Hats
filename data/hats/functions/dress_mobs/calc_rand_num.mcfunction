# Created by Oran9eUtan

execute as @s store result score @s hats_rand_num run data get entity @s Pos[0] 10000
scoreboard players operation @s hats_rand_num %= @s hats_range_up