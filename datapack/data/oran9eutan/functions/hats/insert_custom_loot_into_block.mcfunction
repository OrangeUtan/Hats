# Inserts custom loot from this datapack into a block

execute if block ~ ~ ~ minecraft:chest{LootTable:"minecraft:chests/end_city_treasure"} run loot insert ~ ~ ~ loot hats:chests/end_city_treasure 