setblock ~ 0 ~ oak_sign
data modify block ~ 0 ~ Text1 set value '{"selector": "@p"}'
data modify entity @s Tags prepend from block ~ 0 ~ Text1
data modify entity @s Tags prepend value "OwnerName"
setblock ~ 0 ~ minecraft:air
