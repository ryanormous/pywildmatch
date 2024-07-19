
DESCRIPTION = '''
TEST WHETHER A PATTERN MATCHES A STRING OF TEXT.
GIVE ARGUMENT FOR EITHER --pattern OR --file.
AN ARGUMENT FOR --text IS REQUIRED.
'''

EPILOG = '''
USAGE:
 -p, --pattern)
    THIS IS THE MATCH PATTERN.

 -f, --file)
    PATH TO GITIGNORE FILE.
    TEST WHETHER PATTERNS IN THIS FILE MATCH AGAINST A STRING.

 -t, --text)
    ‹REQUIRED›
    THE STRING AGAINST WHICH A MATCH PATTERN IS TESTED.

 -m, --match)
    ‹OPTIONAL›
    THIS IS THE TYPE OF PATTERN MATCHING. ALSO CALLED MATCH FLAG.
    FLAGS:
       fn, FN)
          PATTERN MATCHING APPROXIMATES PYTHON FNMATCH IMPLEMENTATION.
       wm, WM)
          ‹DEFAULT›
          PATTERN MATCHING LIKE GIT WILDMATCH.
       pw, PW)
          PYWILDMATCH MATCHING, LIKE GIT WILDMATCH BUT PATTERN
          MATCHES ALL CHARACTERS, INCLUDING "/".

 -i, --ignorecase)
    ‹OPTIONAL›
    DEFAULT IS CASE SENSITIVE.

 -V, --version)
    VERSION STRING.

 -h, --help)
    ‹OH CAROLINE NO›
'''


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

import argparse
import re

from pywildmatch import __version__
from pywildmatch.const import *
from pywildmatch.error import (
    MatchFlagArgumentError,
    MatchFlagError
)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# GLOBAL

MAX_FLAG = PW_MATCH + ICASE
FLAG_RANGE = range(FN_MATCH, MAX_FLAG+1)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# CMDLINE ARGUMENT

# MATCH FLAG FROM Namespace OBJ
def get_match_flag(namespace:argparse.Namespace) -> int:
    if namespace.flag.isnumeric():
        flag = int(namespace.flag)
        if flag in FLAG_RANGE:
            return flag
        raise MatchFlagError(MAX_FLAG)
    fnmatch_arg = re.compile(r'fn\w*?', re.I)
    if fnmatch_arg.match(namespace.flag):
        return FN_MATCH
    wildmatch_arg = re.compile(r'wm\w*?|wild.\w*?', re.I)
    if wildmatch_arg.match(namespace.flag):
        return WM_MATCH
    pywildmatch_arg = re.compile(r'pw\w*?|pywild.\w*?', re.I)
    if pywildmatch_arg.match(namespace.flag):
        return PW_MATCH
    raise MatchFlagArgumentError


def getarg() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        add_help = True,
        description = DESCRIPTION,
        epilog = EPILOG,
        formatter_class = argparse.RawDescriptionHelpFormatter,
        usage = argparse.SUPPRESS
    )
    group = parser.add_mutually_exclusive_group(
        required = True
    )
    group.add_argument(
        '-p', '--pattern',
        action = 'store',
        dest = 'pattern',
        metavar = '<PATTERN>'
    )
    group.add_argument(
        '-f', '--file',
        action = 'store',
        dest = 'ignorefile',
        metavar = '<IGNOREFILE>'
    )
    parser.add_argument(
        '-t', '--text',
        action = 'store',
        dest = 'text',
        metavar = '<TEXT>',
        required = True
    )
    # OPTIONAL
    parser.add_argument(
        '-m', '--match',
        action = 'store',
        default = str(WM_MATCH),
        dest = 'flag',
        metavar = '<MATCH FLAG>',
    )
    parser.add_argument(
        '-i', '--ignorecase',
        action = 'store_true',
        dest = 'icase'
    )
    parser.add_argument(
        '-V', '--version',
        action = 'version',
        version = f'version {__version__}'
    )
    # NAMESPACE
    namespace = parser.parse_args()
    namespace.flag = get_match_flag(namespace)
    return namespace

