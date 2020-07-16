# Replace leather helmet hats on armor stands nearby with stick hats
execute as @e[type=minecraft:armor_stand,distance=0..8,tag=!global.ignore] if predicate oran9eutan:hats/entity/wears_leather_helmet_hat run function oran9eutan:hats/hat_mechanism/equip_armorstand_with_correct_hat

advancement revoke @s only oran9eutan:hats/event/player_interacted_with_armor_stand