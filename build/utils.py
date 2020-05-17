import os, re

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