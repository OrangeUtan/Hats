# Created by Oran9eUtan

execute as @s[nbt={VillagerData:{profession:"minecraft:librarian"}}] run function hats:dress_mobs/villagers/librarian


#------------------------------------#
# Add optional cat hat and cat offer #
#------------------------------------#
execute as @s[nbt=!{VillagerData:{profession:"minecraft:none"}}] run function hats:dress_mobs/villagers/add_favorite_cat


#------------------------------------------------#
# Only tag villagers with professions as dressed #
#------------------------------------------------#
execute as @s[nbt=!{VillagerData:{profession:"minecraft:none"}}] run tag @s add hats_is_dressed