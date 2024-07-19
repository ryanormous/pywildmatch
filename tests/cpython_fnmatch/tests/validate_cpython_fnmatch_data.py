
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

import re
from fnmatch import translate


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# TEST MATCH

def decode(txt):
    return txt.decode('latin-1') if hasattr(txt, 'decode') else txt


def fnmatch(pattern, text, flag):
    regexp = translate(decode(pattern))
    patObj = re.compile(
        regexp,
        re.IGNORECASE if (flag & 1) else 0
    )
    result = patObj.match(decode(text))
    return bool(result)


def test_match(pattern, text, flag, expected):
    result = fnmatch(pattern,text,flag)
    assert result == expected

