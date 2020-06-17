# Recursively advances a raycast until either it hits a chest or it reached its max distance

# Summon a marker at the hit chest
execute if block ~ ~ ~ chest align xyz positioned ~.5 ~.5 ~.5 run summon minecraft:area_effect_cloud ~ ~ ~ {Duration:1,Radius:0,Tags:["hats.raycast.hit"]}

# Advance ray
scoreboard players remove #raysteps hatsMath 1
execute if score #raysteps hatsMath matches 0.. unless block ~ ~ ~ chest positioned ^ ^ ^0.2 run function hats:utils/raycast_for_chest_rec