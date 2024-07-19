
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

import os
import pytest
from subprocess import DEVNULL, Popen


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# libgit2 EXECUTABLE

libgit2_tests_dir = os.path.dirname(os.path.realpath(__file__))

libgit2_dir = os.path.dirname(libgit2_tests_dir)

wildmatch_exe = os.path.join(libgit2_dir, 'bin', 'wildmatch.bin')


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# TEST MATCH

def assert_wildmatch_exe_exists():
    make = os.path.join(libgit2_dir, 'wildmatch')
    msg = f'''
        libgit2 WILDMATCH EXECUTABLE NOT FOUND: {wildmatch_exe!r}
        TRY RUNNING make FROM {make!r}
    '''
    if not os.path.lexists(wildmatch_exe):
        pytest.exit(1, msg)


def match_cmd(pattern, text, flag):
    cmd = [wildmatch_exe, pattern, text, str(flag)]
    popen = Popen(cmd, stdout=DEVNULL, stderr=DEVNULL)
    popen.communicate()
    return True if popen.returncode == 0 else False


def test_match(pattern, text, flag, expected):
    assert_wildmatch_exe_exists()
    result = match_cmd(pattern,text,flag)
    assert result == expected

