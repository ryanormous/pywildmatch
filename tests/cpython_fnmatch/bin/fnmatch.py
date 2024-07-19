
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

import re
import fnmatch

from pywildmatch.arg import getarg
from pywildmatch.const import *
from pywildmatch.logger import (
    get_std_logger,
    cpython_fnmatch_ParamFormatter
)
from pywildmatch.error import MatchFlagError
from pywildmatch.param import KeyParam


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# GLOBAL

MAX_FLAG = FN_MATCH + ICASE


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# PYTHON FNMATCH

def decode(txt):
    return txt.decode('latin-1') if hasattr(txt, 'decode') else txt


def log(param):
    logger = get_std_logger()
    formatter = cpython_fnmatch_ParamFormatter(logger)
    logger.debug(formatter.format(param))


def match(param):
    try:
        patObj = re.compile(
            param.regexp,
            re.IGNORECASE if (param.flag & 1) else 0
        )
    except Exception as e:
        result = e
    else:
        try:
            result = patObj.match(decode(param.text))
        except Exception as e:
            result = e
    param.update(result)


def main():
    arg = getarg()
    if arg.flag > MAX_FLAG:
        raise MatchFlagError(arg.flag, MAX_FLAG)
    param = KeyParam(
        pattern = arg.pattern,
        regexp = fnmatch.translate(decode(arg.pattern)),
        text = arg.text,
        flag = arg.flag
    )
    match(param)
    log(param)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# MAIN

if __name__ == '__main__':
    main()

