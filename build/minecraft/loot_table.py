import json

class TableType:
    EMPTY = "minecraft:empty"
    ENTITY = "minecraft:entity"
    BLOCK = "minecraft:block"
    CHEST = "minecraft:chest"
    FISHING = "minecraft:fishing"
    ADVANCEMENT_REWARD = "minecraft:advancement_reward"
    GENERIC = "minecraft:generic"

class EntryType:
    ITEM = "minecraft:item"
    TAG = "minecraft:tag"
    LOOT_TABLE = "minecraft:loot_table"
    GROUP = "minecraft:group"
    ALTERNATIVES = "minecraft:alternatives"
    SEQUENCE = "minecraft:sequence"
    DYNAMIC = "minecraft:dynamic"
    EMPTY = "minecraft:empty"

def loot_table(type=None, pools=None):
    loot_table = json.loads("{}")
    if type:
        loot_table['type'] = type
    if pools:
        loot_table['pools'] = pools
    return loot_table

def entry(entry=None, conditions=None, type=None, name=None, children=None, expand=None, functions=None, weight=None, quality=None):
    if not entry:
        entry = json.loads("{}")
    if conditions:
        entry['conditions'] = conditions
    if type:
        entry['type'] = type
    if name:
        entry['name'] = name
    if children:
        entry['children'] = children
    if expand:
        entry['expand'] = expand
    if functions:
        entry['functions'] = functions
    if weight:
        entry['weight'] = weight
    if quality:
        entry['quality'] = quality
    return entry

def pool(conditions=None, rolls=None, bonus_rolls=None, entries=None):
    pool = json.loads("{}")
    if conditions: 
        pool['conditions'] = conditions
    if rolls:
        pool['rolls'] = rolls
    if bonus_rolls:
        pool['bonus_rolls'] = bonus_rolls
    if entries:
        pool['entries'] = entries
    return pool

def generate_all_entries(entries):
    return list(map((lambda e: pool(entries=[e], rolls=1)), entries))

def generate_random_entry(entries):
    return [pool(rolls=1, entries=entries)]