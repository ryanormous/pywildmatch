
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# pywildmatch CONTSTANT

# match.Match FLAG
FN_MATCH:  int = 0
ICASE:     int = 1
WM_MATCH:  int = 2
PW_MATCH:  int = 4


# param.Param MATCH RESULT
NO_MATCH:  int = ord('∅') # CHARACTER 8709 # «EMPTY SET»
MATCH:     int = ord('∈') # CHARACTER 8712 # «ELEMENT OF SET»
NEG_MATCH: int = ord('∉') # CHARACTER 8713 # «NOT AN ELEMENT OF SET»


# __all__
__all__ = [
    'FN_MATCH',
    'ICASE',
    'WM_MATCH',
    'PW_MATCH',
    'NO_MATCH',
    'MATCH',
    'NEG_MATCH'
]

