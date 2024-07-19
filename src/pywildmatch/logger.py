
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

import logging
import re
import sys
from collections.abc import Iterator
from typing import TypeAlias

from pywildmatch.const import *
from pywildmatch.param import Parameter


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# PARAMETER FORMATTING

class StrSeq:
    MatchType: TypeAlias = re.Match[str]
    find_ctrl = getattr(
        re.compile('[\x00-\x20\x7f-\xa0]'),
        'finditer'
    )

    def __init__(self, charSeq:str) -> None:
        self.charSeq = charSeq

    def __call__(self) -> str:
        return self.get_printable_seq()

    # REPRESENT CONTROL CHARACTER
    def get_ctrl_char(self, char:str) -> str:
        return {
            '\x00': '<NULL>',
            '\x07': '<BELL>',
            '\x08': '<BACK>',
            '\x09': '<TAB>',
            '\x0a': '<NEWLINE>',
            '\x0b': '<VTAB>',
            '\x0c': '<FORMFEED>',
            '\x0d': '<RETURN>',
            '\x20': '<SPACE>'
        }.get(char, '<CONTROL>')

    # FIND CONTROL CHARACTERS
    def iter_ctrl(self) -> Iterator[MatchType]:
        yield from self.find_ctrl(self.charSeq)

    def get_printable_seq(self) -> str:
        buf,pos = str(),0
        for i in self.iter_ctrl():
            buf += self.charSeq[pos:i.start()]
            buf += self.get_ctrl_char(i.group(0))
            pos = i.end()
        buf += self.charSeq[pos:]
        return buf


class BytesSeq:
    MatchType: TypeAlias = re.Match[bytes]
    find_ctrl = getattr(
        re.compile(b'[\x00-\x20\x7f-\xa0]'),
        'finditer'
    )

    def __init__(self, charSeq:bytes) -> None:
        self.charSeq = charSeq

    def __call__(self) -> bytes:
        return self.get_printable_seq()

    # REPRESENT CONTROL CHARACTER
    def get_ctrl_char(self, char:bytes) -> bytes:
        return {
            b'\x00': b'<NULL>',
            b'\x07': b'<BELL>',
            b'\x08': b'<BACK>',
            b'\x09': b'<TAB>',
            b'\x0a': b'<NEWLINE>',
            b'\x0b': b'<VTAB>',
            b'\x0c': b'<FORMFEED>',
            b'\x0d': b'<RETURN>',
            b'\x20': b'<SPACE>'
        }.get(char, b'<CONTROL>')

    # FIND CONTROL CHARACTERS
    def iter_ctrl(self) -> Iterator[MatchType]:
        yield from self.find_ctrl(self.charSeq)

    def get_printable_seq(self) -> bytes:
        buf,pos = bytes(),0
        for i in self.iter_ctrl():
            buf += self.charSeq[pos:i.start()]
            buf += self.get_ctrl_char(i.group(0))
            pos = i.end()
        buf += self.charSeq[pos:]
        return buf


class ParamFormatter:
    # REMOVE FORMATTING FROM REGULAR EXPRESSION RESULT
    patObj_beg = re.compile(r'^re\.compile\(\'')
    patObj_end = re.compile(r'\'\)$|\', re\.IGNORECASE\)$')
    # FLAG MODIFIER STRING, PLACEHOLDER
    flag_modifier = str()
    # LOGGING HANDLER
    handler = str()

    def __init__(self, logger:logging.Logger) -> None:
        for handler in logger.handlers:
            if isinstance(handler, logging.StreamHandler):
                name = getattr(handler.stream, 'name', str())
                if isinstance(name, str) and 'stdout' in name:
                    self.handler = 'stdout'
                    return

    # MAKE CHARACTER SEQUENCE PRINTABLE, ESPECIALLY NON-VISIBLE CHARACTERS
    def make_printable(self, param:Parameter, attr:str) -> str|bytes:
        try:
            seq = getattr(param, attr)
        except AttributeError:
            return str()
        return BytesSeq(seq)() if isinstance(seq, bytes) else StrSeq(seq)()

    # RESULT
    def get_param_result(self, param:Parameter) -> str:
        return {
            NO_MATCH: chr(NO_MATCH).join((
                '\x1b[1;31m', '\x1b[0m'
            )) if self.isatty else chr(NO_MATCH),
            MATCH: chr(MATCH).join((
                '\x1b[1;32m', '\x1b[0m'
            )) if self.isatty else chr(MATCH)
        }.get(param.result, chr(param.result))

    # SPAN
    def get_param_span(self, param:Parameter) -> str:
        span = getattr(param, 'span', (0,0))
        return repr(span) if max(span) > 0 else str()

    # REGX
    def get_param_regx(self, param:Parameter) -> str:
        regx = getattr(param, 'regexp', str())
        return self.patObj_end.sub(
            '', self.patObj_beg.sub('', regx)
        ) if regx and self.patObj_beg.match(regx) else regx

    # OPTS
    def get_param_opts(self, param:Parameter) -> str:
        flag = param.flag
        opts = {
            FN_MATCH: 'fnmatch',
            WM_MATCH: 'wildmatch',
            PW_MATCH: 'pywildmatch',
        }.get(flag - (flag & ICASE), str())
        if flag & ICASE:
            opts += ',ignorecase'
        if getattr(param, 'negate', False):
            opts += ',negate'
        if self.flag_modifier:
            opts = self.flag_modifier + opts
        return opts

    # FORMATTED ATTRIBUTES FOR Parameter
    def format(self, param:Parameter) -> str:
        i = param.__slots__.index('flag')
        keys = param.__slots__[:i]
        paramObj = dict(zip(
            keys, (getattr(param, k, None) for k in keys)
        ))
        paramObj.update({
            'result': self.get_param_result(param),
            'pattern': self.make_printable(param, 'pattern'),
            'regexp': self.get_param_regx(param),
            'text': self.make_printable(param, 'text'),
            'span': self.get_param_span(param),
            'opts': self.get_param_opts(param)
        })
        buf = ''
        for key,val in paramObj.items():
            if not val:
                continue
            if key != 'result':
                val = repr(val)
            buf += f'{key.upper()[:6]}:\t{val}\n'
        return buf

    @property
    def isatty(self) -> bool:
        return all((
            self.handler == 'stdout',
            sys.stdout.isatty(),
            not hasattr(sys, 'ps1')
        ))


# USED BY tests/fnmatch/main.py
class cpython_fnmatch_ParamFormatter(ParamFormatter):
    flag_modifier: str = 'cpython_'


# USED BY tests/libgit2/main.py
class libgit2_ParamFormatter(ParamFormatter):
    flag_modifier: str = 'libgit2_'


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# LOGGER

def get_std_logger() -> logging.Logger:
    loglevel = logging.DEBUG
    stream = sys.stdout
    handler = logging.StreamHandler(stream)
    handler.setLevel(loglevel)
    logger = logging.getLogger('pywildmatch')
    logger.addHandler(handler)
    logger.setLevel(loglevel)
    return logger


def get_logger(logname:str=str()) -> logging.Logger:
    if logname == 'root' or logging.root.manager.loggerDict.get(logname):
        # LOG TO logname
        logger = logging.getLogger(f'{logname}.pywildmatch')
        logger.addHandler(logging.NullHandler())
        return logger
    # LOG TO stdout
    return get_std_logger()

