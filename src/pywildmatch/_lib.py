
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# pywildmatch CONTSTANT

from sre_constants import SRE_FLAG_IGNORECASE as IGNORECASE

# param.Param MATCH RESULT
NO_MATCH  = ord('∅') # 8709 # `EMPTY SET` CHARACTER
MATCH     = ord('∈') # 8712 # `ELEMENT OF SET` CHARACTER
NEG_MATCH = ord('∉') # 8713 # `NOT AN ELEMENT OF SET` CHARACTER

# match.Match FLAG
FN_Match  = 0
WM_Match  = 2
ALL_Match = 4


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# pywildmatch FUNCTION

from sre_compile import compile as sre_compile

# SRE TOKENIZER IMPLICITLY DECODES BYTES OBJECTS AS latin-1
def decode(s): # -> str
    try:
        return s.decode('latin-1')
    except AttributeError:
        return s


