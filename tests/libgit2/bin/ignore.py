
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

import re
import os
from configparser import RawConfigParser
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

MAX_FLAG = ICASE
parent = os.path.dirname(os.path.realpath(__file__))
ignore_exe = os.path.join(parent, 'ignore.bin')


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# libgit2 IGNORE

def log(param):
    logger = get_std_logger()
    formatter = libgit2_ParamFormatter(logger)
    logger.debug(formatter.format(param))


def isfile(ignorefile):
    return os.path.isfile(
        os.path.realpath(
            os.path.expanduser(ignorefile)
    ))


def read_ignorefile(ignorefile):
    parser = RawConfigParser(dict_type=dict, strict=False)
    parser.SECTCRE = re.compile(r'(?P<header>.+)')
    with open(ignorefile) as fd:
        parser.read_file(fd)
    return '\n'.join(parser.sections())


def get_flag(param):
    flag = (param.flag + ICASE) if (
        param.icase and not (param.flag & ICASE)
    ) else param.flag
    if flag > MAX_FLAG:
        raise MatchFlagError(MAX_FLAG)
    return flag


def run(pattern, text, flag):
    cmd = [ignore_exe, pattern, text, str(flag)]
    popen = Popen(cmd, stdout=NULL, stderr=NULL)
    popen.communicate()
    return popen.returncode


def ignore(param):
    ignorefile = read_ignorefile(param.pattern) \
        if isfile(param.pattern) else param.pattern
    flag = get_flag(param)
    result = run(ignorefile, param.text, flag)
    if result == 0:
        param.update(re.compile('').match(''))
    else:
        param.update(None)


def main():
    arg = getarg()
    if arg.flag > MAX_FLAG:
        raise MatchFlagError(arg.flag,MAX_FLAG)
    if not arg.ignorefile:
        raise PatternArgumentError
    param = KeyParam(
        pattern=arg.ignorefile,
        text=arg.text,
        flag=arg.flag,
        icase=arg.icase,
        ignore=True
    )
    ignore(param)
    log(param)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# MAIN

if __name__ == '__main__':
    make = os.path.join(os.path.dirname(parent), 'ignore')
    assert os.path.lexists(ignore_exe), f'''
        libgit2 IGNORE EXECUTABLE NOT FOUND: {ignore_exe!r}
        TRY RUNNING make FROM {make!r}
    '''
    main()

