
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

from pywildmatch import Match
from pywildmatch.error import InputError, WildmatchError
from pywildmatch.param import Param


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# PYWILDMATCH

max_flag = 5

def match(pattern, text, flag):
    try:
        matcher = Match().match_one(pattern, flag)
    except (InputError, WildmatchError) as e:
        param = Param(
            pattern = pattern,
            text = text,
            flag = flag
        )
        param.update(e)
        return param
    try:
        param = matcher(text)
    except WildmatchError as e:
        param = Param(
            pattern = pattern,
            text = text,
            flag = flag
        )
        param.update(e)
    return param


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# MAIN

if __name__ == '__main__':
    import runpy
    runpy.run_module('pywildmatch', run_name='__main__')

