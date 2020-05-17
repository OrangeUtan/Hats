###############################################################################
# as: Player                                                                  #  
# Descr: Replace #hat_on_head item, that the Player took from their own head, #
#        with a #hat item                                                     #
###############################################################################

# Miscellaneous
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3000}}]}] run function hats:fix_hat/fez
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3001}}]}] run function hats:fix_hat/squid
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3002}}]}] run function hats:fix_hat/arrow
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3003}}]}] run function hats:fix_hat/frying_pan

# Tophats
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3100}}]}] run function hats:fix_hat/tophats/white
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3101}}]}] run function hats:fix_hat/tophats/orange
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3102}}]}] run function hats:fix_hat/tophats/magenta
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3103}}]}] run function hats:fix_hat/tophats/light_blue
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3104}}]}] run function hats:fix_hat/tophats/yellow
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3105}}]}] run function hats:fix_hat/tophats/lime
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3106}}]}] run function hats:fix_hat/tophats/pink
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3107}}]}] run function hats:fix_hat/tophats/gray
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3108}}]}] run function hats:fix_hat/tophats/light_gray
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3109}}]}] run function hats:fix_hat/tophats/cyan
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3110}}]}] run function hats:fix_hat/tophats/purple
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3111}}]}] run function hats:fix_hat/tophats/blue
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3112}}]}] run function hats:fix_hat/tophats/brown
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3113}}]}] run function hats:fix_hat/tophats/green
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3114}}]}] run function hats:fix_hat/tophats/red
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3115}}]}] run function hats:fix_hat/tophats/black
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3116}}]}] run function hats:fix_hat/tophats/rainbow
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3117}}]}] run function hats:fix_hat/tophats/black_monocle

# Cats
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3120}}]}] run function hats:fix_hat/cats/ocelot
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3121}}]}] run function hats:fix_hat/cats/tabby
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3122}}]}] run function hats:fix_hat/cats/tuxedo
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3123}}]}] run function hats:fix_hat/cats/red
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3124}}]}] run function hats:fix_hat/cats/siamese
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3125}}]}] run function hats:fix_hat/cats/british_shorthair
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3126}}]}] run function hats:fix_hat/cats/calico
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3127}}]}] run function hats:fix_hat/cats/persian
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3128}}]}] run function hats:fix_hat/cats/ragdoll
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3129}}]}] run function hats:fix_hat/cats/white
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3130}}]}] run function hats:fix_hat/cats/jellie
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3131}}]}] run function hats:fix_hat/cats/black

# Glasses
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3140}}]}] run function hats:fix_hat/glasses/sunglasses
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3141}}]}] run function hats:fix_hat/glasses/harry_potter
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3142}}]}] run function hats:fix_hat/glasses/half_rim
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3143}}]}] run function hats:fix_hat/glasses/rainbow
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3144}}]}] run function hats:fix_hat/glasses/librarian
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3145}}]}] run function hats:fix_hat/glasses/three_d

# Accessories
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3150}}]}] run function hats:fix_hat/accessories/ninja_headband
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3151}}]}] run function hats:fix_hat/accessories/steve_mask
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3152}}]}] run function hats:fix_hat/accessories/alex_mask
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3153}}]}] run function hats:fix_hat/accessories/snorkel_mask_blue
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3154}}]}] run function hats:fix_hat/accessories/snorkel_mask_red
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3155}}]}] run function hats:fix_hat/accessories/googly_eyes

# Villager related
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3160}}]}] run function hats:fix_hat/villager/armorer
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3161}}]}] run function hats:fix_hat/villager/farmer
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3162}}]}] run function hats:fix_hat/villager/nose

# Mario
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3170}}]}] run function hats:fix_hat/mario/mario_cap
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3171}}]}] run function hats:fix_hat/mario/luigi_cap
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3172}}]}] run function hats:fix_hat/mario/cappy
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3173}}]}] run function hats:fix_hat/mario/toad_red
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3174}}]}] run function hats:fix_hat/mario/toad_blue
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3175}}]}] run function hats:fix_hat/mario/toad_yellow
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3176}}]}] run function hats:fix_hat/mario/toad_green
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3177}}]}] run function hats:fix_hat/mario/mario
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:3178}}]}] run function hats:fix_hat/mario/luigi

# Halloween
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:7773180}}]}] run function hats:fix_hat/halloween/wiggly_ghast
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:7773181}}]}] run function hats:fix_hat/halloween/native_american_headband
execute as @s[nbt={Inventory:[{id:"minecraft:stick",tag:{Tags:["is_hat"],CustomModelData:7773182}}]}] run function hats:fix_hat/halloween/jason_mask