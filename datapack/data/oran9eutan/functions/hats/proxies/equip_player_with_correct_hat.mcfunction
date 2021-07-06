# executor: World
# descr: This function is scheduled as a proxy, so that another function call can be scheduled with a desired context

# Execute proxied function as Players with helmet hats on their head
execute as @a[tag=!global.ignore] if predicate oran9eutan:hats/entity/wears_inventory_hat run function oran9eutan:hats/hat_mechanism/equip_player_with_correct_hat
