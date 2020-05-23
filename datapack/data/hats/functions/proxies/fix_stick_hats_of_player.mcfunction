# executor: World
# descr: This function is scheduled as a proxy, so that another function call can be scheduled with a desired context

# Execute proxied function as Players with sitck hats in their inventory
execute as @a[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"]}}]}] run function hats:hat_mechanism/fix_stick_hats_of_player