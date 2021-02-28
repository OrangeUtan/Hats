import json
import os
from itertools import chain


def get_json_files(root):
    for root, dirs, files in os.walk(root):
        for file in files:
            _, extension = os.path.splitext(file)
            if extension == ".json":
                yield os.path.join(root, file)


for json_file in chain(get_json_files("datapack"), get_json_files("resourcepack")):
    content = {}
    with open(json_file) as file:
        content = json.load(file)

    with open(json_file, "w") as file:
        json.dump(content, file, separators=[",", ":"])
