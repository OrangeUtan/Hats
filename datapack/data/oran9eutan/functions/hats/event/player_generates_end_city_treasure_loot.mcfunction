# Raycast for the chest the Player is currently looking at
execute anchored eyes run function oran9eutan:hats/utils/raycast_for_chest

# Insert custom loot into the chest
execute if predicate oran9eutan:hats/chests/chance_end_city_treasure at @e[type=area_effect_cloud,distance=..6,tag=hats.raycast.hit,limit=1] run function oran9eutan:hats/insert_custom_loot_into_block
kill @e[type=area_effect_cloud,distance=..6,tag=hats.raycast.hit]

advancement revoke @s only oran9eutan:hats/event/player_generates_end_city_treasure_loot