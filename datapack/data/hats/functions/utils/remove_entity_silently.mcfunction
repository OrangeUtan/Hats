# Kills an entity without showing its death animation or a death message
# executor: Entity to be removed

# Save state of gamerule
execute store result score #gamerule_tmp hatsMath run gamerule showDeathMessages
# Hide death msg of dog
gamerule showDeathMessages false

# Send to a better place :c
tp ~ -100 ~
kill @s

# Reset gamerule to its previous state
execute if score #gamerule_tmp hatsMath matches 1 run gamerule showDeathMessages true
scoreboard players reset #gr_tmp hatsMath