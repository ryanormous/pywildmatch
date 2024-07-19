
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

from re import Match as Mtype
from sre_compile import (
    compile as sre_compile,
    error as RegexError
)
#from re._compiler import compile as sre_compile
#from re._constants import PatternError as RegexError

from pywildmatch.const import *
from pywildmatch.error import *
from pywildmatch.param import Param, Parameter
from pywildmatch.parse import parse


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# GLOBAL

MAX_FLAG = PW_MATCH + ICASE
FLAG_RANGE = range(FN_MATCH, MAX_FLAG+1)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# MATCH PATTERN AGAINST A STRING

class Match:
    __slots__ = ('_match', 'param')

    def __init__(
        self,
        pattern:str|bytes,
        flag:int=WM_MATCH,
        icase:bool=False,
        ignore:bool=False
    ) -> None:
        flag = (flag + ICASE) if (
            icase and not (flag & ICASE)
        ) else flag
        if flag not in FLAG_RANGE:
            raise MatchFlagError(MAX_FLAG)
        if not pattern:
            raise PatternArgumentError
        self._init_param(pattern, flag, ignore)
        self._init_match()

    def __call__(self, text:str|bytes) -> Parameter:
        self.param.text = text
        result = self._match(
            text.decode('latin-1') if hasattr(text, 'decode') else text
        )
        if self.param.negate:
            if self.param.ignore:
                self.param.update(NEG_MATCH if result else None)
            else:
                self.param.update(None if result else NEG_MATCH)
        else:
            self.param.update(result)
        return self.param

    # Parameter OBJ FOR GIVEN PATTERN
    def _init_param(self, pattern:str|bytes, flag:int, ignore:bool) -> None:
        try:
            regexp, method, negate = parse(pattern, flag, ignore)
        except PywildmatchError as e:
            from .log import errexit
            from .param import KeyParam
            param = KeyParam(pattern=pattern, flag=flag, ignore=ignore)
            param.update(e)
            errexit(param)
        self.param = Param(pattern, regexp, method, flag, negate, ignore)

    # REGX MATCH FUNCTION FOR GIVEN Parameter OBJ
    def _init_match(self) -> None:
        try:
            self._match = getattr(
                sre_compile(self.param.regexp),
                self.param.method
            )
        except RegexError as e:
            from .log import errexit
            e.__class__.__name__ = 'RegexError'
            self.param.update(e)
            errexit(self.param)

