
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

import os
import re
import sys
from subprocess import (
    DEVNULL as NULL,
    Popen
)
from tempfile import TemporaryDirectory

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


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# git IGNORE

strip_text = re.compile('\\\\n|\n|\\\\t|\t').sub
splitlines = re.compile('\\\\n|\n').split


def log(param):
    logger = get_std_logger()
    formatter = libgit2_ParamFormatter(logger)
    logger.debug(formatter.format(param))


def get_flag(param):
    flag = (param.flag + ICASE) if (
        param.icase and not (param.flag & ICASE)
    ) else param.flag
    if flag > MAX_FLAG:
        raise MatchFlagError(MAX_FLAG)
    return flag


def git_init(tmp):
    cmd = ['git', 'init', '--quiet']
    popen = Popen(cmd, cwd=tmp, stdout=NULL, stderr=-1)
    _, stderr = popen.communicate()
    if stderr:
        raise RuntimeError(stderr.decode())


def git_ignorecase(tmp):
    cmd = ['git', 'config', 'core.ignorecase', 'true']
    popen = Popen(cmd, cwd=tmp, stdout=NULL, stderr=-1)
    _, stderr = popen.communicate()
    if stderr:
        raise RuntimeError(stderr.decode())


def write_gitignore(ignorefile, tmp):
    with open(f'{tmp}/.gitignore', 'w') as fd:
        fd.write('\n'.join(splitlines(ignorefile)))


def git_checkignore(text, tmp):
    cmd = ['git', 'check-ignore', '--quiet', strip_text('', text)]
    popen = Popen(cmd, cwd=tmp, stdout=NULL, stderr=-1)
    _, stderr = popen.communicate()
    if stderr:
        print(stderr.decode())
    return popen.returncode


def check_ignore(pattern, text, flag):
    tmp = TemporaryDirectory()
    try:
        git_init(tmp.name)
        if flag == 1:
            git_ignorecase(tmp.name)
        write_gitignore(pattern, tmp.name)
        code = git_checkignore(text, tmp.name)
    finally:
        tmp.cleanup()
    return code


def run_cmd(param):
    flag = get_flag(param)
    code = check_ignore(param.pattern, param.text, flag)
    if code == 0:
        param.update(re.compile('').match(''))
    else:
        param.update(None)
    return code


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
    code = run_cmd(param)
    log(param)
    return code


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# MAIN

if __name__ == '__main__':
    sys.exit(main())

