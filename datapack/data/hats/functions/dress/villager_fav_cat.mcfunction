# Add tag to indicate that the villager has a favorite cat
tag @s add hats.villager.has_fav_cat

# Equip a favorite cat, depending on the biome
loot replace entity @s armor.head loot hats:dress/villager_favorite_cat

# Villagers don't drop their favorite cat
data modify entity @s ArmorDropChances[3] set value 0.0f

# Add trade for favorite cat
function hats:add_trades/favorite_cat