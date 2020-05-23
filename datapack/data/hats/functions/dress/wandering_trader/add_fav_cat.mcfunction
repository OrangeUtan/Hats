# Add tag to indicate that the villager has a favorite cat
tag @s add hats.mob.has_fav_cat

# Equip Wandering Trader with random cat
loot replace entity @s armor.head loot hats:hat_on_head/cats/_rand

# Wandering Traders don't drop their favorite cat
data modify entity @s ArmorDropChances[3] set value 0.0f

# Add trade for favorite cat
function hats:dress/wandering_trader/add_fav_cat_trade