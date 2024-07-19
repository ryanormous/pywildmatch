
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

from re import Match as Mtype

from pywildmatch.const import *


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# INPUT OUTPUT PARAMETERS FOR "match" FUNCTION
#  pattern
#    WILDMATCH PATTERN
#  regexp
#    REPRESENTATION OF pattern AS REGULAR EXPRESSION
#  method
#    REGULAR EXPRESSION METHOD: search OR match
#  text
#    STRING ASSOCIATED WITH match FUNCTION RESULT
#  span
#    REGULAR EXPRESSION MATCH INDICES, IF ANY
#  group
#    REGULAR EXPRESSION GROUPING, IF ANY
#  error
#    MESSAGE FROM Exception OBJECT
#  flag
#    MATCH FLAG, OPTION PASSED FROM ARGUMENT
#  icase
#    CASE INSENSITIVE FLAG, OPTION PASSED FROM ARGUMENT
#    KeyParam ONLY
#  negate
#    OPTION DERIVED FROM pattern
#  ignore
#    FUNCTIONALITY FOR READING gitignore FILE
#  result
#    CONSEQUENCE OF match FUNCTION RUN AGAINST text

class Parameter:
    error:   str
    flag:    int
    group:   str
    ignore:  bool
    method:  str
    negate:  bool
    pattern: str|bytes
    regexp:  str
    result:  int
    span:    tuple[int, int]
    text:    str|bytes

    # ORDER OF __slots__ HAS MEANING FOR LOG FORMATTER
    __slots__ = (
        'result',
        'pattern',
        'regexp',
        'method',
        'text',
        'span',
        'group',
        'error',
        'flag',
        'negate',
        'ignore'
    )

    def __bool__(self) -> bool:
        return self.result in (MATCH, NEG_MATCH)

    def __repr__(self) -> str:
        param = {
            key:getattr(self, key)
            for key in self.__slots__[1:]
            if hasattr(self, key) and
            getattr(self, key) not in (
                str(), (0,0)
            )
        }
        param['match'] = self.__bool__()
        return repr(param)

    def update(self, obj:object) -> None:
        if obj is None:
            self.result = NO_MATCH
            self.error = str()
            self.group = str()
            self.span = (0,0)
        elif obj is NEG_MATCH:
            # RESULT IS NEGATED MATCH
            self.result = NEG_MATCH
            self.error = str()
            self.group = str()
            self.span = (0,0)
        elif isinstance(obj, Mtype):
            # RESULT IS REGULAR EXPRESSION MATCH
            self.result = MATCH
            self.error = str()
            self.group = obj.group(0) or str()
            self.span = obj.span()
        elif isinstance(obj, BaseException):
            # RESULT IS Exception
            self.result = NO_MATCH
            self.error = f'{obj.__class__.__name__}: {obj.args[0]}'
            self.group = str()
            self.span = (0,0)

    has_match = property(__bool__)


# ‹NO_MATCH› Parameter FOR Ignore
class NullParam(Parameter):
    __slots__ = (
        'result',
        'pattern',
        'regexp',
        'method',
        'text',
        'span',
        'group',
        'error',
        'flag',
        'negate',
        'ignore'
    )
    def __init__(
        self,
        text:  str|bytes,
        flag:  int,
    ) -> None:
        self.text = text
        self.flag = flag
        self.result = NO_MATCH
        self.ignore = True


# Parameter, POSITIONAL ARG INITIALIZER
class Param(Parameter):
    __slots__ = (
        'result',
        'pattern',
        'regexp',
        'method',
        'text',
        'span',
        'group',
        'error',
        'flag',
        'negate',
        'ignore'
    )
    def __init__(
        self,
        pattern: str|bytes,
        regexp:  str,
        method:  str,
        flag:    int,
        negate:  bool,
        ignore:  bool
    ) -> None:
        self.result  = NO_MATCH
        self.pattern = pattern
        self.regexp  = regexp
        self.method  = method
        self.flag    = flag
        self.negate  = negate
        self.ignore  = ignore


# Parameter, KEYWORD ARG INITIALIZER
class KeyParam(Parameter):
    def __init__(
        self,
        result:  int=NO_MATCH,
        pattern: str|bytes=str(),
        regexp:  str=str(),
        method:  str=str(),
        text:    str|bytes=str(),
        span:    tuple[int,int]=(0,0),
        group:   str=str(),
        error:   str=str(),
        flag:    int=WM_MATCH,
        icase:   bool=bool(),
        negate:  bool=bool(),
        ignore:  bool=bool()
    ) -> None:
        self.result  = result
        self.pattern = pattern
        self.regexp  = regexp
        self.method  = method
        self.text    = text
        self.span    = span
        self.group   = group
        self.error   = error
        self.flag    = flag
        self.icase   = icase
        self.negate  = negate
        self.ignore  = ignore

