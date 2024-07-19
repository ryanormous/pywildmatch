
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# DATA

DATA = ((
# WILD, ANYTHING
# 0
    '*',
    '/',
    {
        'test':     (True, True, False, False, False, False),
        'validate': (True, True, False, False)
}), (
# 1
    '**',
    '/',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 2
    '**/foo',
    'bazfoo',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 3
    '?**/**0',
     '_Ab/210',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 4
    'A**/**?',
    'ABc/10_',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 5
    'A**/?**0',
    'ABc/_10',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 6
    'A**?**0',
    'ABc_210',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 7
    'A**?*0',
    'ABc_210',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 8
    'A*?**0',
    'Ab_/210',
    {
        'test':     (True, True, False, False, True, True),
        'validate': (True, True, False, False)
}), (
# 9
    'abc**+z',
    'abcde+z',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 10
    'abc**+z',
    'abcdez',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 11
    'some]t*',
    'some]text',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 12
    '[somet*',
    '[sometext]',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (False, False, False, False) #XXX diff ok
}), (
# 13
    '\[somet*',
    '[sometext]',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 14
    '[somet*]',
    '[sometext]',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# CHARACTER SET
# 15
    'A**/[a-f]**0',
    'A/b0',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 16
    'A**/[a-f]*0',
    'A/b0',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 17
    'A**[a-f]**0',
    'Ab0',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 18
    'A**[a-f]*0',
    'Ab0',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 19
    'A**[a-f]/**0',
    'Ab/0',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 20
    'A**[a-f]/*0',
    'Ab/0',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 21
    'A*/[a-f]**0',
    'A/b0',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 22
    'A*[a-f]**0',
    'Ab0',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 23
    'A*[a-f]/**0',
    'Ab/0',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 24
    'A[a-f]**/**0',
    'Ab/0',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 25
    'A[a-f]**/*0',
    'Ab/0',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 26
    'A[a-f]**0',
    'Ab0',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 27
    'A[a-f]*/**0',
    'Ab/0',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 28
    'X[A-]',
    'XZ',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 29
    'X[Y-]',
    'XZ',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 30
    'X[Y-]',
    'X-',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 31
    '[%--|~]',
    '+',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 32
    '[%--|~]',
    '.',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 33
    '[£-Ø+--]',
    'Ð',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (False, False, False, False) #XXX diff ok
}), (
# 34
    '[£-Ø+--]',
    ',',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 35
    'a[#-0]b',
    'A/b',
    {
        'test':     (False, True, False, False, False, True),
        'validate': (False, True, False, False)
}), (
# 36
    'a[^--9-A-z]b',
    'a:b',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 37
    'a[^--9-A-z]b',
    'a/b',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 38
    'a[--9-A-z]b',
    'a/b',
    {
        'test':     (True, True, False, False, True, True),
        'validate': (True, True, False, False)
}), (
# 39
    'a[\\--9-A-z]b',
    'a/b',
    {
        'test':     (True, True, False, False, True, True),
        'validate': (True, True, False, False)
}), (
# 40
    '[a-c--w-z]',
    ':',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 41
    '[^a-c--w-z]',
    'x',
    {
        'test':     (True, False, True, False, True, False),
        'validate': (True, False, True, False)
}), (
# 42
    '[a-c\\-w-z]',
    'x',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 43
    '[a-c-wz]',
    '-',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 44
    '[a-c-wz]',
    'd',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 45
    '[a-z--]',
    ',',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 46
    '[a-z+--]',
    ',',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 47
    '[z-a+--/Z-A]',
    ',',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 48
    '[z-a+--/Z-A]',
    'x',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (False, False, False, False) #XXX diff ok
}), (
# 49
    '[z-a+--/Z-A]',
    'X',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (False, False, False, False) #XXX diff ok
}), (
# 50
    '[z-a+--/Z-A]',
    '/',
    {
        'test':     (True, True, False, False, True, True),
        'validate': (True, True, False, False)
}), (
# 51
    '[|----B]',
    '/',
    {
        'test':     (True, True, False, False, True, True),
        'validate': (True, True, False, False)
}), (
# 52
    '[|----B]',
    'a',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (False, True, False, True) #XXX diff ok
}), (
# 53
    '[|----B]',
    'z',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (False, False, False, False) #XXX diff ok
}), (
# 54
    '[|----B]',
    '~',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 55
    '[|----B]',
    ',',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 56
    '[#-+-|-----B]',
    ',',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 57
    '[#-+-|-----B]',
    'A',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (False, False, False, False) #XXX diff ok
}), (
# 58
    '[#-+-|-----B]',
    'a',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (False, False, False, False) #XXX diff ok
}), (
# 59
    '[#-+-|-----B]',
    'C',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (False, False, False, False) #XXX diff ok
}), (
# 60
    '[#-+-|-----B]',
    'c',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (False, False, False, False) #XXX diff ok
}), (
# 61
    '[#-+-|-----B]',
    '~',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 62
    '[a-z#+--]',
    ',',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 63
    '[z-a#/--]',
    '.',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (False, False, False, False) #XXX diff ok
}), (
# 64
    '[z-a#/--]',
    '/',
    {
        'test':     (True, True, False, False, True, True),
        'validate': (True, True, False, False)
}), (
# 65
    '[#----Z]',
    '0',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 66
    '[#----Z]',
    '/',
    {
        'test':     (True, True, False, False, True, True),
        'validate': (True, True, False, False)
}), (
# 67
    '[#----Z]',
    '^',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 68
    '[-Z-Z]',
    '-',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 69
    '[-Z-Z]',
    'A',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 70
    '[^#-./-9]',
    '/',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 71
    '[^#-./-9]',
    '0',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 72
    '[a&&b][a&&b][a&&b]',
    'a&b',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 73
    '[+-/-]',
    '/',
    {
        'test':     (True, True, False, False, True, True),
        'validate': (True, True, False, False)
}), (
# 74
    '[/-/]',
    '/',
    {
        'test':     (True, True, 'EmptyCharacterSetError', 'EmptyCharacterSetError', True, True),
        'validate': (True, True, False, False)
}), (
# 75
    '[^/-/]',
    '/',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 76
    '[/-/-]',
    '/',
    {
        'test':     (True, True, False, False, True, True),
        'validate': (True, True, False, False)
}), (
# 77
    '[!]',
    '!',
    {
        'test':     ('EmptyCharacterSetError', 'EmptyCharacterSetError', 'EmptyCharacterSetError', 'EmptyCharacterSetError', 'EmptyCharacterSetError', 'EmptyCharacterSetError'),
        'validate': (False, False, False, False)
}), (
# 78
    '[]',
    '',
    {
        'test':     ('EmptyCharacterSetError', 'EmptyCharacterSetError', 'EmptyCharacterSetError', 'EmptyCharacterSetError', 'EmptyCharacterSetError', 'EmptyCharacterSetError'),
        'validate': (False, False, False, False)
}), (
# 79
    'a[x\]z]',
    'az',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 80
    '[A-F[-z]',
    '[',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 81
    '[A-F[-z]',
    '^',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 82
    '[A-F[-z]',
    'g',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 83
    '[A-F[-z]',
    '-',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 84
    '[J-H-Z]',
    'H',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (False, False, False, False) #XXX diff ok
}), (
# 85
    '[J-H-Z]',
    'I',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (False, False, False, False) #XXX diff ok
}), (
# 86
    '[J-H-Z]',
    'Z',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, False, True, False) #XXX diff ok
}), (
# 87
    '[J-H-Z]',
    'K',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 88
    '[J-H-Z]',
    'Y',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# CHARACTER CLASS
# 89
    't[[:lower:]]s[a-z]i[^[:digit:]]g',
    'testing',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 90
    't[[:lower:]]s[a-z]i[^[:digit:]]g',
    'tEsting',
    {
        'test':     (False, True, False, True, False, True),
        'validate': (False, True, False, True)
}), (
# 91
    'A**[[:digit:]]*0',
    'A10',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 92
    'A**[[:digit:]]0',
    'A10',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 93
    'A*[[:digit:]]*0',
    'A10',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 94
    'A*[[:digit:]]0',
    'A10',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 95
    '[-[:xdigit:]]x-z]',
    'y',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 96
    '[-[[:xdigit:]]x-z]',
    '[x-z]',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 97
    '[-[:xdigit:]]x-z',
    'ax-z',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 98
    '[-[:xdigit:]]x-z]',
    '.',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 99
    '[x-z[[:xdigit:]]',
    'F',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 100
    '[x-z[[:xdigit:]]',
    '[',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 101
    '[X-Y-[:digit:]-y]',
    'z',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 102
    '[X-Y#-[:digit:]_]',
    'A',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 103
    '[X-Y[-[:digit:]]',
    'Z',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 104
    '[X-Y[-[:digit:]]',
    '[',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (False, False, False, False) #XXX diff ok
}), (
# 105
    '[X-Y[-[:digit:]]',
    '-',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (False, False, False, False) #XXX diff ok
}), (
# 106
    '[X-Y[-[:digit:]]',
    '9',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (False, False, False, False) #XXX diff ok
}), (
# 107
    '[[:alpha:]-_`]',
    '^',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 108
    '[[:alpha:]-_`]',
    ']',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 109
    '[[:alpha:]\]-_]',
    '^',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 110
    '[[:alpha:]\]-_]',
    ']',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 111
    'a[[:punct:]]b',
    'a/b',
    {
        'test':     (True, True, False, False, True, True),
        'validate': (True, True, False, False)
}), (
# 112
    'a[^[:alnum:]]b',
    'a/b',
    {
        'test':     (True, True, False, False, True, True),
        'validate': (True, True, False, False)
}), (
# 113
    '[[:punct:]][^[:ascii:]][[:upper:]]or[[:blank:]]Qu[[:lower:]] [[:graph:]]o*',
    '¡¿Por Qué No?!',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (False, False, False, False) #XXX diff ok
}), (
# 114
    'usr\tbin',
    'usr\tbin',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 115
    'usr\\tbin',
    'usr\tbin',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (False, False, False, False) #XXX diff ok
}), (
# 116
    'usr[[:cntrl:]]*',
    'usr\bin',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 117
    'usr[[:punct:]]*',
    'usr\bin',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 118
    'usr[^[:cntrl:]]*n',
    'usr\bin',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 119
    '[[:print:]][[:print:]][[:print:]][[:space:]]c[[:blank:]]z',
    'a b c\tz',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# ESCAPE + ESCAPE
# 120
    'abc**\\\\\\\\z',
    'abcde\\\\\\\\z',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 121
    'A**\\\\**0',
    'Ab&\\\\10',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 122
    'A**\\\\*0',
    'Ab&\\\\10',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 123
    'A*\\\\**0',
    'Ab&\\\\10',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 124
    'A*\\\\\\\\**0',
    'Ab&\\\\\\\\10',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# ESCAPE + SPECIAL CHARACTER
# 125
    'A**\\+**0',
    'Abሴ++ሴ10',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 126
    'A**\\+*0',
    'Abሴ++ሴ10',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 127
    'A*\\+**0',
    'Abሴ++ሴ10',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 128
    'A*\\+\\+**0',
    'Abሴ++ሴ10',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 129
    'abc**\vV',
    'abc000\vV',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 130
    'abc**\\vV',
    'abc000\vV',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (False, False, False, False) #XXX diff ok
}), (
# UNICODE CHARACTER
# 131
    'A**🛧**0',
    'Ab🛧10',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 132
    'A**🛧*0',
    'Ab🛧10',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 133
    'A*🛧**0',
    'Ab🛧10',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# OCTAL
# 134
    'A**\046**Z',
    'A&Z',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 135
    'A**\046*Z',
    'A&Z',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 136
    'A*\046**Z',
    'A&Z',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 137
    'A*\046\046**Z',
    'A&&Z',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# HEX
# 138
    'A**\xff**0',
    'Aÿ0',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 139
    'A**\xff*0',
    'Aÿ0',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 140
    'A*\xff**0',
    'Aÿ0',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 141
    'A*\xff\xff**0',
    'Aÿÿ0',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 16 BIT UNICODE
# 142
    'A**\u0123**Z',
    'AģZ',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 143
    'A**\u0123*Z',
    'AģZ',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 144
    'A*\u0123**Z',
    'AģZ',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 145
    'A*\u0123\u0123**Z',
    'AģģZ',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 32 BIT UNICODE
# 146
    'A**\U00001234**Z',
    'AሴZ',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 147
    'A**\U00001234*Z',
    'AሴZ',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 148
    'A*\U00001234**Z',
    'AሴZ',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 149
    'A*\U00001234\U00001234**Z',
    'AሴሴZ',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# PATTERN NEGATION
# 150
    '!',
    '!',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 151
    '!*',
    '!',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (True, True, True, True) #XXX diff ok
}), (
# 152
    '!*',
    'z',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 153
    '!a',
    'z',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (False, False, False, False) #XXX diff ok
}), (
# 154
    '*!',
    '!',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 155
    '^',
    '^',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 156
    'a["[:digit:]]b',
    'a4b',
    {
        'test':     ('SpecialCharacterError', 'SpecialCharacterError', 'SpecialCharacterError', 'SpecialCharacterError', 'SpecialCharacterError', 'SpecialCharacterError'),
        'validate': (True, True, True, True)
}), (
# 157
    'a[\"[:digit:]]b',
    'a"b',
    {
        'test':     ('SpecialCharacterError', 'SpecialCharacterError', 'SpecialCharacterError', 'SpecialCharacterError', 'SpecialCharacterError', 'SpecialCharacterError'),
        'validate': (True, True, True, True)
}), (
# 158
    'a[\\"[:digit:]]b',
    'a"b',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 159
    'a\44\44bc',
    'a$$bc',
    {
        'test':     ('SpecialCharacterError', 'SpecialCharacterError', 'SpecialCharacterError', 'SpecialCharacterError', 'SpecialCharacterError', 'SpecialCharacterError'),
        'validate': (True, True, True, True)
}), (
# 160
    'a\\44\\44bc',
    'a$$bc',
    {
        'test':     ('CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError'),
        'validate': (False, False, False, False)
}), (
# 161
    'a[\44]?bc',
    'a$$bc',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 162
    'a[\\44]?bc',
    'a$$bc',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (False, False, False, False) #XXX diff ok
}), (
# 163
    'a\$\44bc',
    'a$$bc',
    {
        'test':     ('SpecialCharacterError', 'SpecialCharacterError', 'SpecialCharacterError', 'SpecialCharacterError', 'SpecialCharacterError', 'SpecialCharacterError'),
        'validate': (True, True, True, True)
}), (
# 164
    'a$[\\44]bc',
    'a$$bc',
    {
        'test':     ('SpecialCharacterError', 'SpecialCharacterError', 'SpecialCharacterError', 'SpecialCharacterError', 'SpecialCharacterError', 'SpecialCharacterError'),
        'validate': (False, False, False, False)
}), (
# 165
    'a\$[\\44]bc',
    'a$$bc',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (False, False, False, False)
}), (
# fnmatch — HANDLE '\'  IN CHARACTER SETS
# 166
    r'[\\]',
    '\\',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 167
    r'[!\\]',
    'a',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 168
    r'[!\\]',
    '\\',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}))

