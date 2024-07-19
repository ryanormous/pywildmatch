
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

import re
import os
from subprocess import (
    DEVNULL as NULL,
    Popen
)

from pywildmatch.arg import getarg
from pywildmatch.const import *
from pywildmatch.error import (
    MatchFlagError,
    PatternArgumentError
)
from pywildmatch.logger import (
    get_std_logger,
    libgit2_ParamFormatter
)
from pywildmatch.param import KeyParam


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# GLOBAL

MAX_FLAG = WM_MATCH + ICASE
parent = os.path.dirname(os.path.realpath(__file__))
wildmatch_exe = os.path.join(parent, 'wildmatch.bin')


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# libgit2 WILDMATCH

def log(param):
    logger = get_std_logger()
    formatter = libgit2_ParamFormatter(logger)
    logger.debug(formatter.format(param))


def run(pattern, text, flag):
    cmd = [wildmatch_exe, pattern, text, str(flag)]
    popen = Popen(cmd, stdout=NULL, stderr=NULL)
    popen.communicate()
    return popen.returncode


def get_flag(param):
    flag = (param.flag + ICASE) if (
        param.icase and not (param.flag & ICASE)
    ) else param.flag
    if flag > MAX_FLAG:
        raise MatchFlagError(MAX_FLAG)
    return flag


def match(param):
    flag = get_flag(param)
    result = run(param.pattern, param.text, flag)
    if result == 0:
        param.update(re.compile('').match(''))
    else:
        param.update(None)


def main():
    arg = getarg()
    if not arg.pattern:
        raise PatternArgumentError
    param = KeyParam(
        pattern=arg.pattern,
        text=arg.text,
        flag=arg.flag,
        icase=arg.icase
    )
    match(param)
    log(param)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# MAIN

if __name__ == '__main__':
    make = os.path.join(os.path.dirname(parent), 'wildmatch')
    assert os.path.lexists(wildmatch_exe), f'''
        libgit2 WILDMATCH EXECUTABLE NOT FOUND: {wildmatch_exe!r}
        TRY RUNNING make FROM {make!r}
    '''
    main()

