
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

from pywildmatch.arg import getarg
from pywildmatch.const import *
from pywildmatch.error import PatternArgumentError
from pywildmatch.ignore import Ignore
from pywildmatch.log import log
from pywildmatch.match import Match
from pywildmatch.param import KeyParam


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# COMMAND TEST

def main() -> None:
    arg = getarg()
    if arg.ignorefile:
        # MATCH gitignore PATTERNS AGAINST A STRING
        param = Ignore(arg.ignorefile, arg.flag, arg.icase)(arg.text)
        if param is None:
            param = KeyParam(
                pattern=arg.pattern,
                text=arg.text,
                flag=arg.flag,
                icase=arg.icase,
                ignore=True,
                result=NO_MATCH
            )
    elif arg.pattern:
        # MATCH ONE PATTERN AGAINST A STRING
        param = Match(arg.pattern, arg.flag, arg.icase)(arg.text)
    else:
        raise PatternArgumentError
    log(param)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# MAIN

if __name__ == '__main__':
    main()

