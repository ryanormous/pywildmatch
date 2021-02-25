
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

from fnmatch import translate

from pywildmatch._lib import *
from pywildmatch.param import Param


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# PYTHON FNMATCH

max_flag = 1

def match(pattern, text, flag):
    regx = translate(decode(pattern))
    icase = IGNORECASE if (flag&1) else 0
    param = Param(
        pattern = pattern,
        text = text,
        regx = regx,
        flag = flag
    )
    try:
        result = sre_compile(regx, icase).match(decode(text))
    except Exception as e:
        result = e
    param.update(result)
    return param


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# MAIN

if __name__ == '__main__':
    from pywildmatch.arg import get_args
    from pywildmatch.disp import disp
    args = get_args()
    param = match(
        args.pattern,
        args.text,
        args.flag
    )
    disp(param)


