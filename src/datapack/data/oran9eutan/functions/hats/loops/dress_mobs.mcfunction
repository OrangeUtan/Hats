# Dress all mobs near all Players. Mobs in viewing direction are prioritized
execute as @a[tag=!global.ignore] at @s positioned ^ ^ ^25 run function oran9eutan:hats/dress/dress_mobs_near_player

# loop
execute if {{ hats.setting["dress_mobs"].is_true }} run schedule function oran9eutan:hats/loops/dress_mobs 5s
