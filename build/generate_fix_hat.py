import re
from build.datapack_utils import *

def extract_custom_model_data(filepath):
    with open(filepath, "r") as file:
        cmd_id = re.findall("CustomModelData\s*:(\d{1,7})",file.read())[0]
        return cmd_id

pack_name = "hats"
loot_tables_dir = "data/hats/loot_tables/hat"
outdir = "data/hats/functions/fix_hat"

loot_tables = get_files_in(loot_tables_dir, re_filename="(?!^_).*" , extension=".json")

for lt in loot_tables:
    cmd_id = extract_custom_model_data(lt)
    ingame_path = get_ingame_path(lt, "hats")
    out_file = outdir + '/' + ingame_path.replace("hats:hat/", "") + ".mcfunction"
    
    header = "###################################################\n"\
             "# as: Player                                      #\n"\
             "# Descr: Replace #hat item with #hat_on_head item #\n"\
             "###################################################"

    lines = "clear @s minecraft:stick{{Tags:[\"is_hat\"],CustomModelData:{0}}} 1\n"\
            "execute as @s run loot give @s loot {1}".format(cmd_id, ingame_path)

    data = header + '\n\n' + lines 

    if not os.path.exists(os.path.split(out_file)[0]):
        os.makedirs(os.path.split(out_file)[0])

    with open(out_file, "w") as file:
        file.write(data)
