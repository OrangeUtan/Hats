# Dress all mobs near all Players. Mobs in viewing direction are prioritized
execute as @a at @s positioned ^ ^ ^25 run function hats:dress_mobs/dress_mobs_near_player

schedule function hats:every_5s 5s