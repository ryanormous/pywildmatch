
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

from pywildmatch._lib import *
from pywildmatch.error import InputError, MatchFlagError
from pywildmatch.parse import parse

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# GLOBAL

matchType = type(sre_compile('').match(''))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# INPUT OUTPUT PARAMETERS FOR "matcher" FUNCTION
#  pattern
#    WILDMATCH PATTERN
#  regx
#    REPRESENTATION OF pattern AS REGULAR EXPRESSION
#  method
#    REGULAR EXPRESSION METHOD: search OR match
#  text
#    STRING ASSOCIATED WITH matcher RESULT
#  span
#    REGULAR EXPRESSION MATCH INDICES, IF ANY
#  group
#    REGULAR EXPRESSION GROUPING, IF ANY
#  error
#    MESSAGE FROM Exception OBJECT
#  flag
#    OPTION PASSED FROM ARGUMENT
#  negate
#    OPTION DERIVED FROM pattern
#  result
#    CONSEQUENCE OF matcher RUN AGAINST text

class Param:
    # ORDER OF slots HAS MEANING FOR disp()
    __slots__ = (
        'result',
        'pattern',
        'regx',
        'method',
        'text',
        'span',
        'group',
        'error',
        'flag',
        'negate'
    )
    _type = lambda self,obj: type(obj) is matchType
    _match = (MATCH, NEG_MATCH)

    def __init__(
        self,
        pattern = None,
        regx    = None,
        method  = None,
        text    = None,
        span    = None,
        group   = None,
        error   = None,
        flag    = None,
        negate  = None
    ):
        self.pattern = pattern
        self.regx    = regx
        self.method  = method
        self.text    = text
        self.span    = span
        self.group   = group
        self.error   = error
        self.flag    = flag
        self.negate  = negate
        self.result  = NO_MATCH

    def __bool__(self):
        return self.result in self._match

    has_match = property(__bool__)

    def update(self, obj=None): # -> None
        if obj is None:
            # RESULT IS None OR update() CALLED
            self.result = NO_MATCH
            self.error = self.group = self.span = None
        elif obj is NEG_MATCH:
            # RESULT IS NEGATED MATCH
            self.result = obj
            self.error = self.group = self.span = None
        elif self._type(obj):
            # RESULT IS REGULAR EXPRESSION OBJ
            self.result = MATCH
            self.group = obj.group() or None
            self.span = obj.span() or None
            self.error = None
        elif isinstance(obj, BaseException):
            # RESULT IS Exception
            self.result = obj.__class__.__name__
            self.error = obj.args[0]
            self.group = self.span = None


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# PARAMETERIZE

def parameterize(pattern, flag): # -> Param Type
    if not pattern:
        raise InputError
    if flag not in (
        FN_Match, FN_Match+1,
        WM_Match, WM_Match+1,
        ALL_Match, ALL_Match+1
    ):
        raise MatchFlagError
    pat = decode(pattern)
    # WM_Match
    if flag - (flag&1) == WM_Match:
        pat = parse.sub_wild2(pat)
    # PARSE
    parts = parse.parse(pat, flag)
    # NEGATE
    if parts[0] == 'NEGATE':
        parts.pop(0)
        negate = True
    else:
        negate = False
    # WM_Match
    if flag - (flag&1) == WM_Match:
        parse.demote_match(parts)
        parse.conditional_slash(parts)
    # SET GROUPING
    parse.setgroup(parts)
    # METHODDEF
    if parts[0] == 'WILD2':
        method = 'search'
    else:
        method = 'match'
    # THE END
    parse.fin(parts)
    # REGULAR EXRESSION
    regx = r''.join(p.value for p in parts)
    # PARAMETER OBJECT FROM PATTERN
    return Param(
        pattern = pattern,
        regx = regx,
        method = method,
        flag = flag,
        negate = negate
    )

