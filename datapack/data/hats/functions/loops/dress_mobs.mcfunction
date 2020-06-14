# Dress all mobs near all Players. Mobs in viewing direction are prioritized
execute as @a at @s positioned ^ ^ ^25 run function hats:dress/dress_mobs_near_player

# loop
execute if score #opt_dress_mobs hatsConfig matches 1 run schedule function hats:loops/dress_mobs 5s