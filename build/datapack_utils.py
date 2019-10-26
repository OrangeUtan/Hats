import os, json, re, itertools
from functools import reduce

def get_files_in(path, re_filename=None, extension=None):
    """Returns and filters files contained in a folder recursively"""
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            if re_filename and not re.match(re_filename, filename):
                continue
            listOfFiles.append(os.path.join(dirpath, filename))

    if extension:
        listOfFiles = [file for file in listOfFiles if os.path.splitext(file)[1] == extension]

    return listOfFiles

def filename_from_path(path):
    """ Extracts the filename without the extension from a path """
    return os.path.splitext(os.path.basename(path))[0]

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