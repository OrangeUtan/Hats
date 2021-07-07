# Determines if the Player has any #hat_head items in their inventory and then fixes them
# @s: Player whose #hat_head hats are going to be fixed

# Store the Players inventory
data modify storage hats buffer.inv set from entity @s Inventory
# #hat_head hats on the Players head shold not get fixed
data remove storage minecraft:hats buffer.inv[{Slot:103b}]

execute if data storage minecraft:hats buffer.inv[{id:"{{ hats.default_item_head }}", tag:{Tags:["hats.hat"]}}] run function oran9eutan:hats/hat_mechanism/fix_players_head_hats

# Clean up
data remove storage minecraft:hats buffer
