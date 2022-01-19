# as: The Villager beeing dressed
# descr: Dress the Villager with a random hat and give it hat trades

# Add optional favorite cat hat
execute if predicate oran9eutan:hats/villager/chance_has_fav_cat run function oran9eutan:hats/dress/villager/add_fav_cat

# Add optional trade depending on profession
execute if predicate oran9eutan:hats/villager/can_have_profession_trade if predicate oran9eutan:hats/villager/chance_has_profession_trade run function oran9eutan:hats/dress/villager/add_profession_trade

#--------------------------#
# Mark Villager as dressed #
#--------------------------#
tag @s add hats.mob.dont_dress
