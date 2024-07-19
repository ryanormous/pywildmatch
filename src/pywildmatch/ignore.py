
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

from collections.abc import Iterator as Iter
from configparser import RawConfigParser
from copy import copy
from os import path
#from re._compiler import compile as sre_compile
from sre_compile import compile as sre_compile

from pywildmatch.const import *
from pywildmatch.error import PatternArgumentError
from pywildmatch.match import Match
from pywildmatch.param import Parameter, NullParam


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# MATCH IGNORE PATTERNS

class Re:
    splitlines = getattr(
        sre_compile('\\\\n|\n'),
        'split'
    )
    ends_escaped_space = getattr(
        sre_compile('(\\x5c+)[\x09\x20]+$'),
        'search'
    )
    strip_space = getattr(
        sre_compile('(?<!\\x5c)[\x09\x20]+$'),
        'sub'
    )
    is_comment = getattr(
        sre_compile('^\s*#'),
        'match'
    )


class Ignore:
    __slots__ = ('patterns', 'flag')

    def __init__(
        self,
        ignorefile:str|bytes,
        flag:int=WM_MATCH,
        icase:bool=False
    ) -> None:
        if self._isfile(ignorefile):
            self.patterns = tuple(
                Match(p, flag, icase, ignore=True)
                for p in self._read_ignorefile(ignorefile)
            )
        else:
            self.patterns = tuple(
                Match(p, flag, icase, ignore=True)
                for p in self._splitlines(ignorefile)
            )
        if not self.patterns:
            raise PatternArgumentError
        self.flag = (flag + ICASE) if (
            icase and not (flag & ICASE)
        ) else flag

    def __call__(self, text:str|bytes) -> Parameter:
        null = NullParam(text, self.flag)
        has_match: Parameter = null
        is_negated = False
        for match in self.patterns:
            param = match(text)
            if param.result == MATCH:
                if is_negated:
                    return param
                if not has_match:
                    has_match = copy(param)
            elif param.result == NEG_MATCH and has_match:
                is_negated = True
                has_match = null
            else:
                continue
        return has_match

    def _isfile(self, ignorefile:str|bytes) -> bool:
        return path.isfile(path.realpath(path.expanduser(ignorefile)))

    def _read_ignorefile(self, ignorefile:str|bytes) -> Iter[str]:
        parser = RawConfigParser(dict_type=dict, strict=False)
        parser.SECTCRE = sre_compile(r'(?P<header>.+)')
        with open(ignorefile) as fd:
            parser.read_file(fd)
        yield from parser.sections()

    def _splitlines(self, ignorefile:str|bytes) -> Iter[str]:
        if isinstance(ignorefile, bytes):
            ignorefile = ignorefile.decode('latin-1')
        lines: list[str] = []
        append = lines.append
        for i in Re.splitlines(ignorefile):
            if not i or Re.is_comment(i):
                continue
            end = Re.ends_escaped_space(i)
            if end and end.group(0).count('\\') % 2:
                # ODD ESCAPES
                append(Re.strip_space('', i))
            else:
                append(i.rstrip())
        yield from lines

