# executor: World
# descr: This function is scheduled as a proxy, so that another function call can be scheduled with a desired context

# Execute proxied function as Players with helmet hats on their head
execute as @a[tag=!global.ignore,nbt={Inventory:[{Slot:103b,id:"minecraft:leather_helmet",tag:{Tags:["hats.hat"]}}]}] run function oran9eutan:hats/hat_mechanism/equip_player_with_correct_hat