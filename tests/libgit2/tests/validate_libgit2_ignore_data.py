
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

import os
import pytest
from subprocess import DEVNULL, Popen


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# libgit2 EXECUTABLE

libgit2_tests_dir = os.path.dirname(os.path.realpath(__file__))

libgit2_dir = os.path.dirname(libgit2_tests_dir)

ignore_exe = os.path.join(libgit2_dir, 'bin',  'ignore.bin')


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# TEST IGNORE

def assert_ignore_exe_exists():
    make = os.path.join(libgit2_dir, 'ignore')
    msg = f'''
        libgit2 IGNORE EXECUTABLE NOT FOUND: {ignore_exe!r}
        TRY RUNNING make FROM {make!r}
    '''
    if not os.path.lexists(ignore_exe):
        pytest.exit(1, msg)


def ignore_cmd(pattern, text, flag):
    cmd = [ignore_exe, pattern, text, str(flag)]
    popen = Popen(cmd, stdout=DEVNULL, stderr=DEVNULL)
    popen.communicate()
    return True if popen.returncode == 0 else False


def test_ignore(pattern, text, flag, expected):
    assert_ignore_exe_exists()
    result = ignore_cmd(pattern,text,flag)
    assert result == expected

