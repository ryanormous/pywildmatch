
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

from sre_constants import error as sre_error

from pywildmatch._lib import *
from pywildmatch.error import WildmatchError
from pywildmatch.param import Param, parameterize


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# MATCH

class Match:
    def __init__(self, flag=WM_Match, icase=False, verbose=False):
        if not (flag&1) and icase:
            self.flag = flag+1
        else:
            self.flag = flag
        self.verbose = verbose

    # GET Param OBJ FOR GIVEN PATTERN
    def get_param(self, pattern, flag): # -> Param Type
        try:
            return parameterize(pattern, flag)
        except WildmatchError as e:
            if self.verbose:
                from .disp import disp
                param = Param(pattern=pattern, flag=flag)
                param.update(e)
                disp(param)
            raise

    # GET REGX FUNCTION FOR GIVEN Param OBJ
    def get_re(self, param): # -> Pattern
        try:
            return getattr(
                sre_compile(
                    param.regx,
                    IGNORECASE if (param.flag&1) else 0
                ),
                param.method
            )
        except sre_error as e:
            if self.verbose:
                from .disp import disp
                e.__class__.__name__ = 'sre_error'
                param.update(e)
                disp(param)
            raise

    # MATCH ONE PATTERN AGAINST A STRING
    def match_one(self, pattern, flag=None): # -> FunctionType
        flag = self.flag if flag is None else flag
        param = self.get_param(pattern, flag)
        re = self.get_re(param)
        def matcher(text):
            param.text = text
            result = re(decode(text))
            if param.negate:
                if result:
                    param.update()
                else:
                    param.update(NEG_MATCH)
            else:
                param.update(result)
            return param
        return matcher

    # MATCH ANY FROM PATTERNS AGAINST A STRING
    def match_any(self, patterns): # -> FunctionType
        matchers = [self.match_one(p) for p in patterns]
        hit = None
        def matcher(text):
            nonlocal hit
            param = miss = None
            if hit:
                param = hit(text)
                if param.has_match:
                    return param
                miss,hit = hit,None
            for i,m in enumerate(matchers):
                param = m(text)
                if param.has_match:
                    hit = matchers.pop(i)
                    break
            if miss:
                matchers.insert(0, miss)
            if hit:
                return param
        return matcher

    # MATCH EACH FROM PATTERNS AGAINST A STRING
    def match_many(self, patterns): # -> FunctionType
        matchers = (self.match_one(p) for p in patterns)
        mmany = lambda text: (m(text) for m in matchers)
        def matcher(text):
            yield from (param for param in mmany(text) if param)
        return matcher


