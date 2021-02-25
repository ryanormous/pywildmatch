
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

from configparser import RawConfigParser

from pywildmatch._lib import *


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# READ CONFIGURATION FILE

def read_gitignore(file):
    parser = RawConfigParser(dict_type=dict)
    parser.SECTCRE = sre_compile(r'(?P<header>.+)')
    with open(file) as fd:
        parser.read_file(fd)
    return parser.sections()


