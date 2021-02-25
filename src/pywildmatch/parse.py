
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

# SUPPRESS WARNING FOR sre_parse.py ~LINE 585
#   '''FutureWarning: Possible set difference at position %d'''
# Warning is about use of the "-" character inside a character set.
#from warnings import simplefilter
#simplefilter(action='ignore', category=FutureWarning)

import sre_parse
from sre_constants import BRANCH, SUBPATTERN

from pywildmatch._lib import *
from pywildmatch.error import *


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# GLOBAL

ESCAPE = chr(92)
ESCAPE2 = ESCAPE+ESCAPE

CAT = set(
    i.lstrip(ESCAPE)
    for i in sre_parse.CATEGORIES
)

ESC = set(
    i.lstrip(ESCAPE)
    for i in sre_parse.ESCAPES
    if i != ESCAPE2
)

BAD_ESCAPE = sre_parse.ASCIILETTERS - (CAT | ESC)

DIGITS = sre_parse.DIGITS

CHARACTER_CLASS = {
    'alnum': r'\w',
    'alpha': 'A-Za-z',
    'blank': r'\s',
    'cntrl': r'\x00-\x1f\x7f-\xa0',
    'digit': r'\d',
    'graph': r'\S',
    'lower': 'a-z',
    'print': r'\S',
    'punct': r'\W',
    'space': r'\s',
    'upper': 'A-Z',
    'xdigit': r'\dA-Fa-f'
}

# cpython/Objects/unicodeobject.c
MAX_UNICODE = int('0x10FFFF', 16) + 1


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# PARTS

class Partlist:
    __slots__ = (
        '_append',
        '_getitem',
        '_iter',
        '_len',
        '_index',
        '_pop',
        '_repr',
        '_setitem'
    )
    def __init__(self):
        parts = []
        self._append = parts.append
        self._getitem = parts.__getitem__
        self._iter = parts.__iter__
        self._len = parts.__len__
        self._index = parts.index
        self._pop = parts.pop
        self._repr = parts.__repr__
        self._setitem = parts.__setitem__

    def __getitem__(self, i):
        return self._getitem(i)

    def __iter__(self):
        return self._iter()

    def __len__(self):
        return self._len()

    def __repr__(self):
        return self._repr()

    def __setitem__(self, index, value):
        return self._setitem(index, value)

    def append(self, part):
        self._append(part)

    # GET PART BY INDEX
    def get_part(self, index):
        try:
            return self._getitem(index)
        except IndexError:
            return

    def index(self, part, i):
        return self._index(part, i)

    # ITERATE BY PART
    def iter_part(self, part, i=-1, stop=None):
        while True:
            try:
                i = self[:stop].index(part, i+1)
            except ValueError:
                return
            yield i

    def pop(self, i):
        return self._pop(i)


class Part(str):
    __slots__ = ('name', 'value')

    def __str__(self):
        return self.name

    def __new__(cls, name, value=str()):
        self = super().__new__(cls, name)
        self.name = name
        self.value = value
        return self


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# SCAN

class Scan:
    # SUPPORTED SPECIAL CHARACTERS
    YEP = (
        '/'
        r'\!'
        r'\*'
        r'\+'
        r'\.'
        r'\?'
        r'\['
        r'\\'
        r'\]'
        r'\^'
    )
    # NOT SUPPORTED
    NOPE = (
        '$'
        '('
        ')'
        r"\'"
        r'\"'
        r'\{'
        r'\|'
        r'\}'
    )
    LEXICON = ((
        'NOPE', '[' + NOPE + ']'
    ), (
        'ESCAPE', r'\\{1,2}'
    ), (
        'CHARSET_BEGIN', r'\[(?!:[a-z]{5,6}:\])'
    ), (
        'CHARSET_END', r'(?<![a-z]{5}:)\]'
    ), (
        'CHAR_CLASS', r'\[:[a-z]{5,6}:\]'
    ), (
        'ANYTHING', r'\?'
    ), (
        'CARET', r'\^'
    ), (
        'DOT', r'\.'
    ), (
        'NEGATE', r'\!'
    ), (
        'PLUS', r'\+'
    ), (
        'SLASH', '/+' # 1 OR MORE
    ), (
        'WILD', r'\*'
    ), (
        'OK', '[^' + YEP + NOPE + ']+'
    ), (
        'UNHANDLED', r'[\d\D]'
    ))

    def _scan_init(self):
        p = []
        try:
            state = sre_parse.State()
        except AttributeError:
            # python < 3.8.0
            state = sre_parse.Pattern()
        for name,regx in self.LEXICON:
            group = state.opengroup(name)
            re = sre_parse.parse(regx)
            data = [(
                SUBPATTERN, (group, 0, 0, re)
            )]
            p.append(
                sre_parse.SubPattern(state, data)
            )
            state.closegroup(group, p[-1])
        data = [(
            BRANCH, (None, p)
        )]
        return state, data

    def scan(self, pattern):
        match = self._scanner(pattern).match
        i = 0
        while True:
            m = match()
            if not m:
                break
            j = m.end()
            if i == j:
                break
            yield (m.lastgroup, m)
            i = j
        if pattern[i:]:
            raise ParseError(pattern,i)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# STATIC METHODS

class ParseStatic:
    # GUESS ESCAPE SEQUENCE
    guess_hexdig = sre_compile(r'x[\dA-Fa-f]{2}').match
    guess_octdig = sre_compile('[0-7]{3}').match
    guess_ucode = sre_compile(r'u[\dA-Fa-f]{4}').match
    guess_Ucode = sre_compile(r'U[\dA-Fa-f]{8}').match

    ends_escape = sre_compile(r'([^\\])\\$').search
    _sub_wild2 = sre_compile(r'\*\*/(\*\*/)*').sub

    # SUBSTITUE REPETITIONS OF WILD2  "**/**/" -> "**/"
    @staticmethod
    def sub_wild2(pat): # -> str
        return ParseStatic._sub_wild2('**/', pat)

    # LIKE libgit2 WM_PATHNAME
    @staticmethod
    def demote_match(parts): # -> None
        for i in parts.iter_part('WILD2', 0):
            next_part = parts.get_part(i+1)
            if next_part:
                # NOT END
                if next_part != 'SLASH':
                    parts[i] = Part('WILD', '([^/]*)')
            else:
                # END
                prev_part = parts.get_part(i-1)
                if prev_part != 'SLASH':
                    parts[i] = Part('WILD', r'([^/]*\Z)')

    # LIKE libgit2 WM_PATHNAME
    @staticmethod
    def conditional_slash(parts): # -> None
        length = len(parts)
        indexes = []
        for i in parts.iter_part('WILD2', stop=length-1):
            n1 = i+1
            if n1 == length:
                break
            if parts.get_part(n1) == 'SLASH':
                indexes.append(n1)
                n2 = i+2
                if parts.get_part(n2) == 'WILD2':
                    indexes.append(n2)
        # POP CONDITIONAL 'SLASH' PARTS
        indexes.sort(reverse=True)
        for i in indexes:
            parts.pop(i)

    @staticmethod
    def _segment(part): # -> Union[int, None]
        if part != 'OK':
            return
        val = part.value
        index = prev_char = None
        i = -1
        for char in reversed(val):
            if char == ESCAPE:
                if prev_char == ESCAPE:
                    index = i
                    break
                else:
                    i -= 1
                    index = None
            elif index:
                break
            else:
                index = i
                i -= 1
            prev_char = char
        if index and len(val) + index > 0:
            return index

    # ESTABLISH REGULAR EXPRESSION GROUPING
    @staticmethod
    def setgroup(parts): # -> None
        end = len(parts) - 1
        last_i = 0
        segment = ParseStatic._segment
        for i in parts.iter_part('WILD2', 0, end):
            # PART PREVIOUS WILD2
            p = i-1
            prev = parts.get_part(p)
            seg = segment(prev)
            if seg:
                # SEGMENT prev IF SEGMENTABLE
                parts[p].value = '(?:'.join((
                    parts[p].value[:seg],
                    parts[p].value[seg:]
                ))
            elif prev == 'CHARSET_END':
                # INDEX CHARSET_BEGIN
                setbeg = max(parts.iter_part('CHARSET_BEGIN', last_i, i))
                parts[setbeg].value = '(?:' + parts[setbeg].value
            else:
                pp = p-1
                prev_prev = parts.get_part(pp)
                if prev_prev == 'ESCAPE':
                    parts[pp].value = '(?:' + parts[pp].value
                else:
                    parts[p].value = '(?:' + parts[p].value
            parts[i].value = '.*?)'
            # LAST WILD2 INDEX
            last_i = i

    # THE END
    @staticmethod
    def fin(parts): # -> None
        end = parts[-1]
        if end == 'WILD':
            parts[-1].value = r'([^/]*\Z)'
        elif end != 'WILD2':
            parts[-1].value += '$'
        else:
            # ENDS 'WILD2'
            parts[-1].value = '.*?'


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# PARSE

class Parse(Scan, ParseStatic):
    def __init__(self):
        self._scanner = sre_compile(
            sre_parse.SubPattern(*self._scan_init())
        ).scanner

    # FOR PYTHON REGULAR EXPRESSION ESCAPE HANDLING
    def _validate_escape(self, obj): # -> None
        text = obj.string[obj.end():]
        try:
            t = text[0]
        except IndexError:
            # ENDING "\\"
            raise CharacterEscapeError(obj)
        if t in DIGITS:
            dig = self.guess_octdig(text)
            if dig and int(dig.group(), 8) < 256:
                return
            raise CharacterEscapeError(obj)
        if t in BAD_ESCAPE:
            if t == 'U':
                dig = self.guess_Ucode(text)
                if dig and int(dig.group()[1:], 16) < MAX_UNICODE:
                    return
            if any((
                t == 'u' and self.guess_ucode(text),
                t == 'x' and self.guess_hexdig(text)
            )):
                return
            raise CharacterEscapeError(obj)

    def _get_charclass(self, obj, inset): # -> str
        try:
            char_c = CHARACTER_CLASS[
                obj.group().split(':')[1]
            ]
        except KeyError:
            raise CharacterClassNameError(obj)
        # CHARACTER_CLASS WILL WORK OUTSIDE OF CHARACTER SET
        # IF NOT EXPRESSING RANGE WITH "-"
        if not inset and '-' in char_c:
            raise CharacterClassSyntaxError(obj)
        return char_c

    def parse(self, pattern, flag): # -> Partlist Type
        parts = Partlist()
        append = parts.append
        inset = False
        for name, obj in self.scan(pattern):
            prev = parts.get_part(-1)
            value = None
            # NOPE
            if name == 'NOPE':
                raise SpecialCharacterError(obj)
            # ESCAPE
            elif name == 'ESCAPE':
                if obj.group() == ESCAPE2:
                    # DOUBLE
                    name = 'OK'
                    # SEE: '\\\_' == '\\\\_'
                    value = ESCAPE2
                else:
                    # SINGLE
                    self._validate_escape(obj)
                    # SEE: '\_' == '\\_'
                    value = ESCAPE
            # CHAR_CLASS
            elif name == 'CHAR_CLASS':
                value = self._get_charclass(obj, inset)
            # CHARSET_BEGIN
            elif name == 'CHARSET_BEGIN':
                if prev == 'ESCAPE':
                    name = 'OK'
                elif inset:
                    raise NestedCharacterSetError(obj)
                else:
                    inset = True
            # CHARSET_END
            elif name == 'CHARSET_END':
                if prev == 'ESCAPE':
                    name = 'OK'
                elif prev == 'CHARSET_BEGIN':
                    raise EmptyCharacterSetError(obj)
                else:
                    inset = False
            # WILD
            elif name == 'WILD':
                if inset or prev == 'ESCAPE':
                    name = 'OK'
                elif prev == 'WILD':
                    parts[-1] = Part('WILD2')
                    continue
                elif prev == 'WILD2':
                    # OTHERWISE "***"
                    continue
                elif flag - (flag&1) == FN_Match:
                    name = 'WILD2'
                    value = ''
                else:
                    value = '([^/]*)'
            # ANYTHING
            elif name == 'ANYTHING':
                if inset or prev == 'ESCAPE':
                    name = 'OK'
                elif flag - (flag&1) == FN_Match:
                    value = '.'
                else:
                    value = '[^/]'
            # CARET
            # DOT
            # PLUS
            elif name in ('CARET', 'DOT', 'PLUS'):
                name = 'OK'
                if any((
                    inset,
                    prev == 'ESCAPE',
                    prev == 'OK' and self.ends_escape(prev.value)
                )):
                    value = obj.group()
                else:
                    value = ESCAPE + obj.group()
            # NEGATE
            elif name == 'NEGATE':
                if prev == 'CHARSET_BEGIN':
                    value = '^'
                if prev != None:
                    name = 'OK'
            # SLASH
            elif name == 'SLASH':
                # VALUE. "/+" 1 OR MORE
                value = '/'
                if prev == 'ESCAPE':
                    name = 'OK'
            # UNHANDLED
            elif name == 'UNHANDLED':
                # THIS ERROR IS UNTESTED
                raise LexiconError(obj)
            # OK
            if name == prev == 'OK':
                parts[-1].value += value \
                    if value is not None else obj.group()
            # APPEND PART
            else:
                append(Part(name, value
                    if value is not None else obj.group()
                ))
        if inset:
            raise BadCharacterSetError(obj)
        return parts


parse = Parse()

