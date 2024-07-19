__version__ = '0.39.1'

# pywildmatch MATCH FLAG
from pywildmatch.const import (
    FN_MATCH,
    ICASE,
    WM_MATCH,
    PW_MATCH
)

from pywildmatch.match import Match
from pywildmatch.ignore import Ignore

__all__ = [
    'FN_MATCH',
    'ICASE',
    'WM_MATCH',
    'PW_MATCH',
    'Ignore',
    'Match'
]

