# executor: Player whose stick hats are going to be fixed
# descr: Determines if the Player has any stick hats that need to be fixed and then fixes them

# Store the Players inventory
data modify storage hats buffer.inv set from entity @s Inventory
# Stick hats on the Players head shold not get fixed
data remove storage minecraft:hats buffer.inv[{Slot:103b}]

execute if data storage minecraft:hats buffer.inv[{id:"minecraft:stick", tag:{Tags:["is_hat"]}}] run function hats:hat_mechanism/fix_players_stick_hats

# Clean up
data remove storage minecraft:hats buffer