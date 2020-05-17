import os, json, re, itertools
from functools import reduce

def get_mc_name(path, basedir):
    segments = os.path.normpath(path).split(os.path.sep)
    for segment in segments:
        segments = segments[1:]
        if segment == basedir:
            break
    return os.path.splitext(reduce((lambda a,b: a+'/'+b), segments))[0]

def get_ingame_path(path, pack_name):
    """ Get ingame path of resource """
    path_segments = os.path.splitext(os.path.normpath(path))[0].split(os.path.sep)
    ingame_path_segments = path_segments[path_segments.index(pack_name):]
    return ingame_path_segments[0] + ':' + reduce((lambda a,b: a + '/' + b), ingame_path_segments[2:])