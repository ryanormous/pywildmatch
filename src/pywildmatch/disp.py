
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

import logging
import sys
from collections import OrderedDict as ODict

from pywildmatch._lib import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# GLOBAL

NAME = __name__.split('.')[-1]


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# PARAMETER FORMATTING

class Ctrl_Byte:
    CTRL = b'<CONTROL>'
    # FIND CONTROL CHARACTERS
    find_ctrl = sre_compile(b'[\x00-\x20\x7f-\xa0]').finditer
    keys = (
        b'\x00',
        b'\x07',
        b'\x08',
        b'\x09',
        b'\x0a',
        b'\x0b',
        b'\x0c',
        b'\x0d',
        b'\x20'
    )
    chars = dict(zip(
        keys, (
            b'<NULL>',
            b'<BELL>',
            b'<BACK>',
            b'<TAB>',
            b'<NEWLINE>',
            b'<VTAB>',
            b'<FORMFEED>',
            b'<RETURN>',
            b'<SPACE>'
    )))
    # REPRESENT CONTROL CHARACTER
    get_char = lambda self,c: self.chars.get(c, self.CTRL)


class Ctrl_Str:
    CTRL = '<CONTROL>'
    # FIND CONTROL CHARACTERS
    find_ctrl = sre_compile(r'[\x00-\x20\x7f-\xa0]').finditer
    keys = (
        '\x00',
        '\x07',
        '\x08',
        '\x09',
        '\x0a',
        '\x0b',
        '\x0c',
        '\x0d',
        '\x20'
    )
    chars = dict(zip(
        keys, (
            '<NULL>',
            '<BELL>',
            '<BACK>',
            '<TAB>',
            '<NEWLINE>',
            '<VTAB>',
            '<FORMFEED>',
            '<RETURN>',
            '<SPACE>'
    )))
    # REPRESENT CONTROL CHARACTER
    get_char = lambda self,c: self.chars.get(c, self.CTRL)


class ParamFormat:
    Ctrl_Byte = Ctrl_Byte()
    Ctrl_Str = Ctrl_Str()
    # REMOVE FORMATTING FROM REGULAR EXPRESSION RESULT
    sub_beg = sre_compile(r'^re\.compile\(\'')
    sub_end = sre_compile(r'\'\)$|\', re\.IGNORECASE\)$')

    # CHARACTER PRINT HELPER
    def printall(self, strType):
        if isinstance(strType, bytes):
            ctrl = self.Ctrl_Byte
            buf = b''
        else:
            ctrl = self.Ctrl_Str
            buf = ''
        pos = 0
        for i in ctrl.find_ctrl(strType):
            buf += strType[pos:i.start()]
            buf += ctrl.get_char(i.group())
            pos = i.end()
        buf += strType[pos:]
        return buf

    # RESULT
    def _format_result(self, param):
        return {
            NEG_MATCH: chr(NEG_MATCH),
            MATCH: chr(MATCH),
            NO_MATCH: chr(NO_MATCH)
        }.get(param.result, param.result)

    # STRING
    def _format_text(self, param):
        text = param.text
        if text is not None:
            return self.printall(text)

    # SPAN
    def _format_span(self, param):
        span = param.span
        if span is None:
            return
        if not max(span):
            # (0, 0)
            return
        return repr(span)

    # PATTERN
    def _format_pattern(self, param):
        pat = param.pattern
        min_len = len(pat) > 1
        if isinstance(pat, bytes):
            ctrl = self.Ctrl_Byte
        else:
            ctrl = self.Ctrl_Str
        if pat.startswith(ctrl.keys):
            pat = ctrl.get_char(pat[0]) + pat[1:]
        if min_len and pat.endswith(ctrl.keys):
            pat = ctrl.get_char(pat[-1]) + pat[:-1]
        return pat

    # REGX
    def _format_regx(self, param):
        r = param.regx
        if r is None:
            return
        if self.sub_beg.match(r):
            return self.sub_end.sub('', self.sub_beg.sub('', r))
        return r

    # OPTS
    def _format_opts(self, param):
        flag = param.flag
        opts = {
            FN_Match: 'fnmatch',
            WM_Match: 'wildmatch',
            ALL_Match: 'all'
        }.get(flag - (flag&1))
        if flag & 1:
            opts += ',ignorecase'
        if param.negate:
            opts += ',negate'
        return opts

    # FORMATTED ATTRIBUTES FOR Param
    def format(self, param):
        i = param.__slots__.index('flag')
        keys = param.__slots__[:i]
        parameter = ODict(zip(
            keys, (getattr(param, k) for k in keys)
        ))
        parameter.update({
            'result': self._format_result(param),
            'pattern': self.printall(param.pattern),
            'regx': self._format_regx(param),
            'text': self._format_text(param),
            'span': self._format_span(param),
            'opts': self._format_opts(param)
        })
        buf = ''
        _format = lambda k,v: '%s:\t%s\n' % (
            k[:6].upper(), v
        )
        for key,val in parameter.items():
            if val is not None:
                buf += _format(key,val)
        return buf


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# LOGGING

def traverse_loggers():
    # LOGGER UNSUITABILE IF...
    #   PLACEHOLDER FOR LOGGER
    #   NO LOGGER PROPAGATION
    dont_use = lambda log: (
        isinstance(log, logging.PlaceHolder)
        or not log.propagate
    )
    # FILE HANDLER
    is_filehandler = lambda hand: (
        isinstance(hand, logging.FileHandler)
    )
    # ROOT LOGGER
    Logger = logging.getLogger()
    # MANAGER
    ManagerDict = Logger.manager.loggerDict
    # LOGGERS
    loggers = []
    # FIND LOGGERS WITH FileHandler
    append = loggers.append
    for log in ManagerDict.keys():
        logger = ManagerDict[log]
        if dont_use(logger):
            continue
        for hand in logger.handlers:
            if is_filehandler(hand):
                append({
                    'name': logger.name,
                    'level': logger.level
                })
    # IN CASE OF MULTIPLE LOGGERS WITH FileHandler,
    # USE LOGGER WITH LOWEST LEVEL, HIGHEST ANCESTRY
    if loggers:
        key = lambda log: (
            log['level'],
            log['name'].count('.')
        )
        logger = sorted(loggers, key=key)[0]
        return logger['name']


def get_logger(logger=None):
    if logger:
        # LOG TO THIS
        return logging.getLogger(logger)
    level = logging.DEBUG
    child_of = lambda LOG: '%s.%s' % (LOG, NAME)
    parent = traverse_loggers()
    if parent:
        # LOG TO FileHandler
        child = child_of(parent)
        logger = logging.getLogger(child)
        logger.setLevel(level)
    else:
        # LOG TO stdout
        stream = sys.stdout
        handler = logging.StreamHandler(stream)
        handler.setLevel(level)
        child = child_of('root')
        logger = logging.getLogger(child)
        logger.addHandler(handler)
        logger.setLevel(level)
    return logger


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# DISPLAY Param OBJECT

logger = get_logger()
formatter = ParamFormat()

def disp(param):
    logger.debug(formatter.format(param))


