# Dress all mobs near all Players. Mobs in viewing direction are prioritized
execute as @a at @s positioned ^ ^ ^25 run function oran9eutan:hats/dress/dress_mobs_near_player

# loop
execute if score #opt_dress_mobs hats.cfg matches 1 run schedule function oran9eutan:hats/loops/dress_mobs 5s