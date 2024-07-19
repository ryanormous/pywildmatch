
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

from collections.abc import Iterator as Iter
from re import Match as Mtype
from typing import Self
from warnings import warn

from sre_compile import compile as sre_compile
#from re._compiler import compile as sre_compile
import sre_constants
#from re import _constants as sre_constants
import sre_parse
#from re import _parser as sre_parse

from pywildmatch.const import *
from pywildmatch.error import *


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# GLOBAL

ESCAPE = chr(92)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# RE

class Scan:
    lexicon: tuple[tuple[str,str], ...]
    subpatterns: list[sre_parse.SubPattern]

    def __init__(self) -> None:
        self.state = sre_parse.State()
        self.append_subpattern()
        self.compile_scanner()

    def append_subpattern(self) -> None:
        append = self.subpatterns.append
        for name,regx in self.lexicon:
            group = self.state.opengroup(name)
            pattern = sre_parse.parse(regx)
            append(
                sre_parse.SubPattern(
                    self.state,
                    [(
                        sre_constants.SUBPATTERN,
                        (group, 0, 0, pattern)
                    )]
                )
            )
            self.state.closegroup(group, self.subpatterns[-1])

    def compile_scanner(self) -> None:
        subpat = sre_parse.SubPattern(
            self.state,
            [(
                sre_constants.BRANCH,
                (None, self.subpatterns)
            )]
        )
        self._scanner = getattr(sre_compile(subpat), 'scanner')

    def scan(self, string:str) -> Iter[tuple[str,Mtype[str]]]:
        end = len(string)
        match = self._scanner(string).match
        while True:
            m = match()
            if m:
                yield (m.lastgroup or str(), m)
            else:
                break
            if m.end() == end:
                break


class CharsetScan(Scan):
    # NOT SUPPORTED
    nope = (
        '\"'
        "\'"
    )
    # SUPPORTED SPECIAL CHARACTERS
    yep = (
        '\&'
        '\-'
        '/'
        '\['
        r'\\'
        '\]'
        '\|'
        '\~'
    )
    lexicon = ((
        'NEGATE', '^[!^]'
    ), (
        'RANGE', r'(\\{2}|\\?[^\\])\-(\\?.)'
    ), (
        'ESCAPE', r'\\+'
    ), (
        'CHARSET_END', '\]'
    ), (
        'CHAR_CLASS', '\[:[a-dglpsux][ac-eg-ik-pr-uw]{4,5}:\]'
    ), (
        'SLASH', '/+'
    ), (
        'CHARSET_SPECIAL', '[&\-\[|~]'
    ), (
        'NOPE', f'[{nope}]'
    ), (
        'OK', f'[^{nope}{yep}]+(?!\-)'
    ))
    subpatterns = list()


class PatternScan(Scan):
    # NOT SUPPORTED
    nope = (
        '$'
        '('
        ')'
        "\'"
        '\"'
        '\{'
        '\}'
    )
    # SUPPORTED SPECIAL CHARACTERS
    yep = (
        '\*'
        '\+'
        '\.'
        '\?'
        '/'
        '\['
        r'\\'
        '\]'
        '\^'
    )
    lexicon = ((
        'ESCAPE', r'\\+'
    ), (
        'CHARSET_BEGIN', '\['
    ), (
        'WILD', '\*+'
    ), (
        'ANYTHING', '\?+'
    ), (
        'CHAR_SPECIAL', '[+.\]^]'
    ), (
        'SLASH', '/+'
    ), (
        'NOPE', f'[{nope}]'
    ), (
        'OK', f'[^{nope}{yep}]+'
    ))
    subpatterns = list()


class Re:
    # TOKENIZE CHARACTER SET
    scan_charset = CharsetScan().scan
    # TOKENIZE MATCH PATTERN
    scan_pattern = PatternScan().scan
    # ITERATE "]" CHARACTER, ACCOUNTING FOR ESCAPE
    find_setend = getattr(
        sre_compile(r'\\*\]'),
        'finditer'
    )
    # SUBSTITUE REPETITION OF WILD2  "**/**/" —> "**/"
    deduplicate_wild2 = getattr(
        sre_compile('\*\*/(\*\*/)*'),
        'sub'
    )
    # "**" + «NON-SLASH» —> "*"
    # ENDING «NON-SLASH» + "**" —> "*"
    promote_wild = getattr(
        sre_compile('\*{2}(?=[^/])|(?<=[^/])\*{2,}\Z'),
        'sub'
    )
    # OMIT "/" CHARACTERS FOLLOWING WILD2, BUT NOT AT BEGINNING OR END
    conditional_slash = getattr(
        sre_compile('(?<=.\*\*)/+(?=.)'),
        'sub'
    )
    # MATCH BEGINNING OF CHARACTER CLASS
    match_charclass = getattr(
        sre_compile(':[a-dglpsux][ac-eg-ik-pr-uw]{4,5}:\]'),
        'match'
    )


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# PARSE

class Part(str):
    name: str
    value: str
    __slots__ = ('name', 'value')

    def __str__(self) -> str:
        return self.name

    def __new__(cls, name:str, value:str=str()) -> Self:
        self = super().__new__(cls, name)
        self.name = name
        self.value = value
        return self


class Parse:
    # ESCAPE NOT ACCEPTED FOR THESE CHARACTERS INSIDE PATTERN
    bad_esc = (
        '0123456789'
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        'bcdeghijklmopqsuwxyz'
    )
    # ESCAPE NOT ACCEPTED FOR THESE CHARACTERS INSIDE CHARACTER SET
    bad_esc_charset = (
        'ABCEFGHIJKLMNOPQRTUVXYZ'
        'ceghijklmopquxyz'
    )

    def __init__(self, pattern:str, flag:int) -> None:
        self.iflag = flag & ICASE
        self.flag = flag - self.iflag
        if self.flag == WM_MATCH:
            pattern = self.substitute_pattern(pattern)
        self._parts: list[Part] = list()
        self.parse_pattern(pattern)

    def substitute_pattern(self, pattern:str) -> str:
        # LIKE libgit2 WM_PATHNAME
        return Re.conditional_slash(
            '', Re.promote_wild(
                '*', Re.deduplicate_wild2(
                    '**/', pattern
        ))) or str()

    def has_setend(self, lookahead:str) -> bool:
        for obj in Re.find_setend(lookahead):
            if not obj.group().count('\\') % 2:
                # FOUND UNESCAPED "]" CHARACTER
                return True
        return False

    def get_charclass(self, obj:Mtype[str], negate:bool) -> str:
        charclass = obj.group().split(':')[1]
        if self.iflag and charclass in ('lower', 'upper'):
            charclass = 'alpha'
        match charclass:
            case 'alnum':
                return '\w'
            case 'alpha':
                return '\x41-\x5a\x61-\x7a\xc0-\xd6\xd8-\xf6\xf8-\xff'
            case 'ascii':
                return '\x09\x0a-\x0d\x20-\x2e\x30-\x7e' if (
                    self.flag == WM_MATCH and not negate # OMIT "/"
                ) else '\x09\x0a-\x0d\x20-\x7e'
            case 'blank':
                # TAB AND SPACE
                return '\x09\x20'
            case 'cntrl':
                return '\x00-\x1f\x7f-\xa0'
            case 'digit':
                return '\d'
            case 'graph':
                # VISIBLE CHARACTERS
                return '\x21-\x2e\x30-\x7e\xa1-\xff' if (
                    self.flag == WM_MATCH and not negate # OMIT "/"
                ) else '\x21-\x7e\xa1-\xff'
            case 'lower':
                return '\x61-\x7a\xdf-\xf6\xf8-\xff'
            case 'print':
                # SPACE + VISIBLE CHARACTERS
                return '\x20-\x2e\x30-\x7e\xa1-\xff' if (
                    self.flag == WM_MATCH and not negate # OMIT "/"
                ) else '\x20-\x7e\xa1-\xff'
            case 'punct':
                return '\x21-\x2e\x3a-\x40\x5b-\x60\x7b-\x7e\xa1-\xbf' if (
                    self.flag == WM_MATCH and not negate # OMIT "/"
                ) else '\x21-\x2f\x3a-\x40\x5b-\x60\x7b-\x7e\xa1-\xbf'
            case 'space':
                return '\s'
            case 'upper':
                return '\x41-\x5a\xc0-\xd6\xd8-\xde'
            case 'xdigit':
                return '\dA-Fa-f'
            case _:
                raise CharacterClassNameError(obj)

    # GET REMAINING STRING FROM OBJECT
    def lookahead(self, obj:Mtype[str], stop:int=0) -> str:
        start = obj.end()
        try:
            return obj.string[start:start+stop if stop else None]
        except IndexError:
            return str()

    def parse_charset(self, charset:str) -> None:
        append = self._parts.append
        negate = False
        for name, obj in Re.scan_charset(charset):
            match name:
                case 'NEGATE':
                    negate = True
                    value = '^'
                case 'RANGE':
                    v1, v2 = obj[1], obj[2]
                    # FIRST VALUE
                    if not v1.startswith(ESCAPE) and v1 in '&-[|~':
                        v1 = ESCAPE + v1
                    # SECOND VALUE
                    if not v2.startswith(ESCAPE):
                        if v2 == ']':
                            lookahead = self.lookahead(obj)
                            if lookahead[:1] == ']':
                                v2 = ESCAPE + ']'
                            else:
                                # NOT A RANGE
                                append(Part('OK', f'{v1}{ESCAPE}-'))
                                append(Part('CHARSET_END', ']'))
                                self.parse_pattern(lookahead)
                                return None
                        elif v2 == '[':
                            lookahead = self.lookahead(obj)
                            if Re.match_charclass(lookahead):
                                # NOT A RANGE
                                append(Part('OK', f'{v1}{ESCAPE}-'))
                                self.parse_charset('[' + lookahead)
                                return None
                            else:
                                v2 = ESCAPE + '['
                        elif v2 in '&-[|~':
                            v2 = ESCAPE + v2
                    # ORDER RANGE VALUES
                    if (
                        v1[0] if not v1.startswith(ESCAPE) else v1[1]
                    ) > (
                        v2[0] if not v2.startswith(ESCAPE) else v2[1]
                    ):
                        v1, v2 = v2, v1
                    # v1 == v2
                    elif (
                        v1[0] if not v1.startswith(ESCAPE) else v1[1]
                    ) == (
                        v2[0] if not v2.startswith(ESCAPE) else v2[1]
                    ):
                        # NOT A RANGE
                        if (
                            self.flag == WM_MATCH and not negate
                        ) and (
                            v1[0] if not v1.startswith(ESCAPE) else v1[1]
                        ) == '/':
                            # "/" NOT COMPATIBLE WITH WM_MATCH FLAG
                            continue
                        append(Part('OK', v1))
                        continue
                    # WM_MATCH FLAG AND "/" FOUND BETWEEN RANGE OF v1 AND v2
                    if (
                        self.flag == WM_MATCH and not negate
                    ) and (
                        v1[0] if not v1.startswith(ESCAPE) else v1[1]
                    ) <= '/' <= (
                        v2[0] if not v2.startswith(ESCAPE) else v2[1]
                    ):
                        if (v1[0] if not v1.startswith(ESCAPE) else v1[1]) < '.':
                            append(Part('RANGE', f'{v1}-.'))
                        elif (v1[0] if not v1.startswith(ESCAPE) else v1[1]) == '.':
                            append(Part('OK', '.'))
                        if (v2[0] if not v2.startswith(ESCAPE) else v2[1]) > '0':
                            value = f'0-{v2}'
                        else:
                            if (v2[0] if not v2.startswith(ESCAPE) else v2[1]) == '0':
                                append(Part('OK', '0'))
                            continue
                    else:
                        value = f'{v1}-{v2}'
                case 'ESCAPE':
                    v = obj.group()
                    num = len(v)
                    if num % 2:
                        # ODD
                        if self.lookahead(obj, 1) in self.bad_esc_charset:
                            raise CharacterEscapeError(obj)
                        if num > 1:
                            append(Part('OK', ESCAPE+ESCAPE))
                        value = ESCAPE
                    else:
                        # EVEN
                        name = 'OK'
                        value = ESCAPE+ESCAPE
                case 'CHARSET_END':
                    lookahead = self.lookahead(obj)
                    if self.prev == 'ESCAPE':
                        self.prev = Part('OK', ESCAPE + ']')
                        continue
                    elif lookahead.startswith(']'):
                        name = 'OK'
                        value = ESCAPE + ']'
                    elif self.prev in ('CHARSET_BEGIN', 'NEGATE'):
                        if self.has_setend(lookahead):
                            # NOT CHARSET END
                            name = 'OK'
                            value = ESCAPE + ']'
                        else:
                            # RESULTING CHARACTER SET EMPTY
                            raise EmptyCharacterSetError(obj)
                    else:
                        if self.flag == WM_MATCH and negate:
                            append(Part('SLASH', '/'))
                        append(Part(name, ']'))
                        self.parse_pattern(lookahead)
                        return None
                case 'CHAR_CLASS':
                    value = self.get_charclass(obj, negate)
                case 'SLASH':
                    if self.flag == WM_MATCH and not negate:
                        continue
                    name = 'OK'
                    value = '/'
                case 'CHARSET_SPECIAL':
                    name = 'OK'
                    value = ESCAPE + obj.group()
                    if self.prev == 'ESCAPE':
                        self.prev = Part('OK', value)
                        continue
                case 'NOPE':
                    if self.prev == 'ESCAPE':
                        self.prev = Part('OK', ESCAPE + obj.group())
                        continue
                    raise SpecialCharacterError(obj)
                case _:
                    value = obj.group()
            # APPEND value IF ‹OK›
            if name == self.prev == 'OK':
                self.prev.value += value
                continue
            # APPEND Part
            append(Part(name, value))

    def parse_pattern(self, pattern:str) -> None:
        append = self._parts.append
        for name, obj in Re.scan_pattern(pattern):
            match name:
                case 'ESCAPE':
                    v = obj.group()
                    num = len(v)
                    if num % 2:
                        # ODD
                        if self.lookahead(obj, 1) in self.bad_esc:
                            raise CharacterEscapeError(obj)
                        if num > 1:
                            append(Part('OK', v[:-1]))
                        value = ESCAPE
                    else:
                        # EVEN
                        name = 'OK'
                        value = v
                case 'CHARSET_BEGIN':
                    if self.prev == 'ESCAPE':
                        self.prev = Part('OK', ESCAPE + '[')
                        continue
                    lookahead = self.lookahead(obj)
                    if self.has_setend(lookahead):
                        append(Part(name, '['))
                        self.parse_charset(lookahead)
                        return None
                    value = ESCAPE + '['
                case 'WILD':
                    num = min(len(obj.group()), 3)
                    if self.prev == 'ESCAPE':
                        self.prev = Part('OK', ESCAPE + '*')
                        num -= 1
                    if num > 1 or self.flag == FN_MATCH:
                        name = 'WILD2'
                        value = '(?%s[\d\D]*?'
                    elif num:
                        name = 'WILD'
                        value = '(?%s[^/]*?'
                    else:
                        continue
                case 'ANYTHING':
                    num = len(obj.group())
                    if self.prev == 'ESCAPE':
                        self.prev = Part('OK', ESCAPE + '?')
                        num -= 1
                    if num:
                        value = num * (
                            '.' if self.flag == FN_MATCH else '[^/]'
                        )
                    else:
                        continue
                case 'CHAR_SPECIAL':
                    name = 'OK'
                    if self.prev == 'ESCAPE':
                        self.prev = Part('OK', ESCAPE + obj.group())
                        continue
                    value = ESCAPE + obj.group()
                case 'SLASH':
                    v = obj.group()
                    if len(v) > 1:
                        name = 'OK'
                    value = v
                case 'NOPE':
                    if self.prev == 'ESCAPE':
                        self.prev = Part('OK', ESCAPE + obj.group())
                        continue
                    raise SpecialCharacterError(obj)
                case _:
                    value = obj.group()
            # APPEND value IF ‹OK›
            if name == self.prev == 'OK':
                self.prev.value += value
                continue
            # APPEND Part
            append(Part(name, value))

    # REGULAR EXPRESSION GROUPING
    @staticmethod
    def set_group(parts:list[Part]) -> None:
        last_i = 0
        for i,part in enumerate(parts[:-1]):
            if not part.value.startswith('(?%s'):
                continue
            # ATOMIC OR NON-CAPTURING GROUP
            part.value = part.value % ('>' if last_i else ':')
            last_i = i
            # CLOSE GROUP
            nextpart = parts[i+1] if parts[i+1] != 'ESCAPE' else parts[i+2]
            if nextpart == 'OK':
                # INDEX FOR SEGMENTATION AT BEGINNING
                seg = 2 if nextpart.value.startswith(ESCAPE) else 1
                nextpart.value = ')'.join((
                    nextpart.value[:seg], nextpart.value[seg:]
                ))
            elif nextpart == 'CHARSET_BEGIN':
                i = parts.index(Part('CHARSET_END'), i)
                parts[i].value += ')'
            else:
                nextpart.value += ')'
        if last_i:
            # NON-CAPTURING GROUP
            parts[last_i].value = parts[last_i].value.replace('>', ':', 1)

    # REGULAR EXPRESSION ANCHOR
    @staticmethod
    def set_anchor(parts:list[Part], flag:int, ignore:bool) -> None:
        # BEGIN
        beg = parts[0]
        if ignore:
            if beg == 'SLASH':
                beg.value = '/?'
            elif beg not in ('WILD', 'WILD2'):
                beg.value = '(^|/)' + beg.value
        if flag & ICASE:
            beg.value = '(?i)' + beg.value
        # END
        end = parts[-1]
        if end == 'WILD':
            end.value = '[^/]*?' if ignore else '[^/]*?$'
        elif end == 'WILD2':
            end.value = '[\d\D]*?$'
        elif ignore:
            if end != 'SLASH':
                end.value += '(/|$)'
        else:
            end.value += '$'

    @property
    def parts(self) -> list[Part]:
        return self._parts[:]

    @property
    def prev(self) -> Part:
        try:
            return self._parts[-1]
        except IndexError:
            return Part(str())

    @prev.setter
    def prev(self, part:Part) -> None:
        self._parts[-1] = part


def parse(pattern:str|bytes, flag:int, ignore:bool) -> tuple[str,str,bool]:
    # SRE TOKENIZER IMPLICITLY DECODES BYTES OBJECTS AS latin-1
    pattern = pattern.decode('latin-1') \
        if hasattr(pattern, 'decode') else pattern
    # NEGATE
    if pattern.startswith('!'):
        pattern = pattern.lstrip('!')
        negate = True
    else:
        negate = False
    # PARSE PATTERN
    parts = Parse(pattern, flag).parts
    # EMPTY PATTERN
    if not parts:
        return ('^!$', 'match', False) if negate else ('^$', 'match', False)
    # SPECIAL CASE FOR gitignore, "/" PATTERN IS ACCEPTED BUT MATCHES NOTHING
    if ignore and len(parts) == 1 and parts[0] == 'SLASH':
        warn(PatternWarning('/'))
        return ('[^\d\D]', 'match', True if negate else False)
    # gitignore PATTERNS MAY BEGIN WITH "!" OR "#", IF ESCAPED
    if ignore and parts[0] == 'ESCAPE' and parts[1].value.startswith(('!', '#')):
        parts.pop(0)
    # METHODDEF
    if parts[0] == 'WILD2':
        if len(parts) > 1:
            parts[0].value = ''
            if all((
                flag - (flag & ICASE) == WM_MATCH,
                parts[1] == 'SLASH'
            )):
                parts[1].value = '(^|/)'
        method = 'search'
    elif ignore and not negate and any((
        len(parts) > 1 and 'SLASH' not in parts[:-1],
        len(parts) == 1 and parts[0] != 'SLASH'
    )):
        method = 'search'
    else:
        method = 'match'
    # GROUPS
    Parse.set_group(parts)
    # ANCHOR
    Parse.set_anchor(parts, flag, ignore)
    # REGULAR EXRESSION
    regexp = ''.join(p.value for p in parts)
    # Parameter INIT VALUES FROM PATTERN AND OPTIONS
    return (regexp, method, negate)

