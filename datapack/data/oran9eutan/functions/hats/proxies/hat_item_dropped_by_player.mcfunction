# @s: Hat item just dropped by a player

execute if {{ hats.setting["pet_conversion"].is_true }} run function oran9eutan:hats/pet_mechanism/convert_hat_to_pet
