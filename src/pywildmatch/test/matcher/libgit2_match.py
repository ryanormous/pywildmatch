
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

from posixpath import dirname, lexists, realpath
from subprocess import Popen

from pywildmatch._lib import *
from pywildmatch.param import Param


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# GLOBAL

# PATH TO wildmatch.exe
# BUILT FROM libgit2, pywildmatch/test/extra/wildmatch_exe.c
DIR = dirname(dirname(realpath(__file__)))
EXE = '/'.join((DIR, 'extra', 'wildmatch.exe'))
assert lexists(EXE), '''
    EXPECTED THIS PATH FOR libgit2 WILDMATCH TEST: %s
''' % EXE

# GENERIC re.Match OBJECT
matchObj = sre_compile('').match('')

max_flag = 3


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# libgit2 WILDMATCH

def run(pattern, text, flag):
    cmd = [EXE, pattern, text, str(flag)]
    PIPE = -1
    popen = Popen(cmd, stdout=PIPE, stderr=PIPE)
    stdout, stderr = popen.communicate()
    code = popen.returncode
    if code == 0:
        return matchObj
    if stderr:
        raise RuntimeError(stderr.decode())
    # RETURN matchObj, None OR Exception LIKE re.match


def match(pattern, text, flag):
    param = Param(
        pattern = pattern,
        text = text,
        flag = flag
    )
    try:
        result = run(
            decode(pattern),
            decode(text),
            str(flag)
        )
    except RuntimeError as e:
        result = e
    param.update(result)
    return param


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# MAIN

if __name__ == '__main__':
    from pywildmatch.disp import disp
    from pywildmatch.arg import get_args
    args = get_args()
    param = match(
        args.pattern,
        args.text,
        args.flag
    )
    disp(param)

