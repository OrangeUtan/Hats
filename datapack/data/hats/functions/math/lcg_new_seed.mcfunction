summon minecraft:area_effect_cloud ~ ~ ~ {Tags:["hats.rng_seed"]}
execute store result score #hats_lcg hats_math run data get entity @e[distance=..1,type=minecraft:area_effect_cloud,tag=hats.rng_seed,limit=1] UUIDMost 0.00000000023283064365386962890625
kill @e[distance=..1,type=minecraft:area_effect_cloud,tag=hats.rng_seed,limit=1]