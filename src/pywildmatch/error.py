
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

import sys
from re import Match as Mtype

from pywildmatch.const import *


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# ERROR

class PywildmatchError(Exception):
    msg = str()
    def __init__(self) -> None:
        super().__init__(self.msg)


class PatternArgumentError(PywildmatchError):
    msg = 'MISSING ARGUMENT FOR MATCH PATTERN.'


class MatchFlagArgumentError(PywildmatchError):
    def __init__(self) -> None:
        sys.tracebacklimit = 0
        self.msg = (
            f'\n  -m, --match FLAG, IF GIVEN, MUST BE ONE OF…'
            f'\n    "fn", "wm", "pw"'
            f'\n  DEFAULT IS "wm".'
        )
        super().__init__()


class MatchFlagError(PywildmatchError):
    MIN_FLAG = FN_MATCH
    MAX_FLAG = PW_MATCH + ICASE

    def __init__(self, flag:int, max_flag:int=MAX_FLAG) -> None:
        self.msg = (
            f'FLAG "{flag}" OUTSIDE OF ACCEPTED '
            f'RANGE: {self.MIN_FLAG} — {max_flag}'
        )
        super().__init__()


class CharacterEscapeError(PywildmatchError):
    def __init__(self, obj:Mtype[str]|Mtype[bytes]) -> None:
        string = str(obj.string)
        end = obj.end()
        pat = string[end-1:end+1]
        self.msg = f'ESCAPE NOT ACCEPTED: {pat!r} '
        if len(string) == end:
            self.msg += 'AT FINAL '
            end -= 1
        self.msg += f'POSITION: {end}'
        super().__init__()


class SpecialCharacterError(PywildmatchError):
    def __init__(self, obj:Mtype[str]|Mtype[bytes]) -> None:
        self.msg = f'CHARACTER NOT ACCEPTED:{obj.group()!r}'
        super().__init__()


class CharacterClassNameError(PywildmatchError):
    def __init__(self, obj:Mtype[str]|Mtype[bytes]) -> None:
        self.msg = f'NO SUCH CHARACTER CLASS:  {obj.group()!r}'
        super().__init__()


class EmptyCharacterSetError(PywildmatchError):
    def __init__(self, obj:Mtype[str]|Mtype[bytes]) -> None:
        self.msg = (
            f'EMPTY CHARACTER SET NOT ACCEPTED.'
            f'  SEE: {obj.string!r}'
        )
        super().__init__()


class PywildmatchWarning(UserWarning):
    msg = str()
    def __init__(self) -> None:
        super().__init__(self.msg)


class PatternWarning(PywildmatchWarning):
    def __init__(self, pattern:str) -> None:
        self.msg = f'IGNORE PATTERN {pattern!r} MATCHES NOTHING.'
        super().__init__()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# __all__

__all__ = [
    'CharacterClassNameError',
    'CharacterEscapeError',
    'EmptyCharacterSetError',
    'MatchFlagArgumentError',
    'MatchFlagError',
    'PatternArgumentError',
    'PywildmatchError',
    'SpecialCharacterError',
    'PatternWarning'
]

