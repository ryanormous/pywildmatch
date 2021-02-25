
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

from pywildmatch._lib import *


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# EXCEPTIONS

class WildmatchError(Exception):
    def __init__(self):
        super().__init__(self.msg)

class InputError(WildmatchError):
    msg = 'MISSING ARGUMENT'

class MatchFlagError(WildmatchError):
    msg = 'FLAG OUTSIDE OF ACCEPTED RANGE: %d - %d ' % (
        FN_Match, ALL_Match + 1
    )

class CharacterSetError(WildmatchError):
    def __init__(self, obj):
        self.msg = self.msg % obj.string
        super().__init__()

class BadCharacterSetError(CharacterSetError):
    msg = 'UNBALENCED BRACES FOR CHARACTER SET.  PATTERN:%s'

class EmptyCharacterSetError(CharacterSetError):
    msg = 'EMPTY CHARACTER SET.  PATTERN:%s'

class NestedCharacterSetError(CharacterSetError):
    msg = 'NESTED CHARACTER SET NOT ACCEPTED.  PATTERN:%s'

class CharacterEscapeError(WildmatchError):
    msg = 'ESCAPE NOT ACCEPTED:%s  INDEX:%s  PATTERN:%s'
    def __init__(self, obj):
        try:
            esc = obj.group() + obj.string[obj.end()]
        except IndexError:
            esc = obj.group()
        self.msg = self.msg % (esc, obj.start(), obj.string)
        super().__init__()

class CharError(WildmatchError):
    def __init__(self, obj):
        self.msg = self.msg % (
            obj.group(),
            obj.start(),
            obj.string
        )
        super().__init__()

class LexiconError(CharError):
    msg = 'FAILED TO HANDLE CHARACTER:%s  INDEX:%s  PATTERN:%s'
    # THIS ERROR IS UNTESTED

class CharacterClassNameError(CharError):
    msg = 'NO SUCH CHARACTER CLASS:%s  INDEX:%s  PATTERN:%s'

class CharacterClassSyntaxError(CharError):
    msg = 'CHARACTER CLASS "%s" MUST BE USED INSIDE'\
        ' CHARACTER SET.  INDEX:%s  PATTERN:%s'

class SpecialCharacterError(CharError):
    msg = 'CHARACTER NOT ACCEPTED:%s  INDEX:%s  PATTERN:%s'

class ParseError(WildmatchError):
    def __init__(self, pat, index):
        self.msg = ' '.join((
            pat, 'INDEX:%s' % index, pat[index:]
        ))
        super().__init__()

