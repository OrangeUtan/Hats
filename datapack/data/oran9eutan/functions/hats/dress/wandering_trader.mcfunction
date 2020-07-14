# executor: The Wandering Trader beeing dressed
# descr: Try to dress the Wandering Trader with a hat and add some trades

# Add optional favorite cat hat
execute if predicate oran9eutan:hats/wandering_trader/chance_has_fav_cat run function oran9eutan:hats/dress/wandering_trader/add_fav_cat

# Add optional Villager trade. This trade offers hats related to Villagers
execute if predicate oran9eutan:hats/wandering_trader/chance_has_villager_trade run function oran9eutan:hats/dress/wandering_trader/add_villager_trade

# Mark Wandering Trader as dressed
tag @s add hats.mob.dont_dress