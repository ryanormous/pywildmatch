
# BASED ON TEST CASES FOR libgit2 wildmatch
# libgit2/tests/util/wildmatch.c
# VERSION: v1.7.0-244


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# DATA

DATA = ((
# BASIC WILDMATCH
# 0
    'foo',
    'foo',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 1
    'bar',
    'foo',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 2
    '',
    '',
    {
        'test':     ('PatternArgumentError', 'PatternArgumentError', 'PatternArgumentError', 'PatternArgumentError', 'PatternArgumentError', 'PatternArgumentError'),
        'validate': (True, True, True, True)
}), (
# 3
    '???',
    'foo',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 4
    '??',
    'foo',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 5
    '*',
    'foo',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 6
    'f*',
    'foo',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 7
    '*f',
    'foo',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 8
    '*foo*',
    'foo',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 9
    '*ob*a*r*',
    'foobar',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 10
    '*ab',
    'aaaaaaabababab',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 11
    'foo\\*',
    'foo*',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 12
    'foo\\*bar',
    'foobar',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 13
    'f\\\\oo',
    'f\\oo',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 14
    '*[al]?',
    'ball',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 15
    '[ten]',
    'ten',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 16
    '**[!te]',
    'ten',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 17
    '**[!ten]',
    'ten',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 18
    't[a-g]n',
    'ten',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 19
    't[!a-g]n',
    'ten',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 20
    't[!a-g]n',
    'ton',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 21
    't[^a-g]n',
    'ton',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 22
    'a[]]b',
    'a]b',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 23
    'a[]-]b',
    'a-b',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 24
    'a[]-]b',
    'a]b',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 25
    'a[]-]b',
    'aab',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 26
    'a[]a-]b',
    'aab',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 27
    ']',
    ']',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# SLASH MATCHING FEATURES
# 28
    'foo*bar',
    'foo/baz/bar',
    {
        'test':     (True, True, False, False, False, False),
        'validate': (True, True, False, False)
}), (
# 29
    'foo**bar',
    'foo/baz/bar',
    {
        'test':     (True, True, False, False, True, True),
        'validate': (True, True, False, False)
}), (
# 30
    'foo**bar',
    'foobazbar',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 31
    'foo/**/bar',
    'foo/baz/bar',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 32
    'foo/**/**/bar',
    'foo/baz/bar',
    {
        'test':     (False, False, True, True, False, False),
        'validate': (False, False, True, True)
}), (
# 33
    'foo/**/bar',
    'foo/b/a/z/bar',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 34
    'foo/**/**/bar',
    'foo/b/a/z/bar',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 35
    'foo/**/bar',
    'foo/bar',
    {
        'test':     (False, False, True, True, False, False),
        'validate': (False, False, True, True)
}), (
# 36
    'foo/**/**/bar',
    'foo/bar',
    {
        'test':     (False, False, True, True, False, False),
        'validate': (False, False, True, True)
}), (
# 37
    'foo?bar',
    'foo/bar',
    {
        'test':     (True, True, False, False, False, False),
        'validate': (True, True, False, False)
}), (
# 38
    'foo[/]bar',
    'foo/bar',
    {
        'test':     (True, True, 'EmptyCharacterSetError', 'EmptyCharacterSetError', True, True),
        'validate': (True, True, False, False)
}), (
# 39
    'foo[^a-z]bar',
    'foo/bar',
    {
        'test':     (True, True, False, False, True, True),
        'validate': (True, True, False, False)
}), (
# 40
    'f[^eiu][^eiu][^eiu][^eiu][^eiu]r',
    'foo/bar',
    {
        'test':     (True, True, False, False, True, True),
        'validate': (True, True, False, False)
}), (
# 41
    'f[^eiu][^eiu][^eiu][^eiu][^eiu]r',
    'foo-bar',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 42
    '**/foo',
    'foo',
    {
        'test':     (False, False, True, True, False, False),
        'validate': (False, False, True, True)
}), (
# 43
    '**/foo',
    'XXX/foo',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 44
    '**/foo',
    'bar/baz/foo',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 45
    '*/foo',
    'bar/baz/foo',
    {
        'test':     (True, True, False, False, False, False),
        'validate': (True, True, False, False)
}), (
# 46
    '**/bar*',
    'foo/bar/baz',
    {
        'test':     (True, True, False, False, False, False),
        'validate': (True, True, False, False)
}), (
# 47
    '**/bar/*',
    'deep/foo/bar/baz',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 48
    '**/bar/*',
    'deep/foo/bar/baz/',
    {
        'test':     (True, True, False, False, False, False),
        'validate': (True, True, False, False)
}), (
# 49
    '**/bar/**',
    'deep/foo/bar/baz/',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 50
    '**/bar/*',
    'deep/foo/bar',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 51
    '**/bar/**',
    'deep/foo/bar/',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 52
    '**/bar**',
    'foo/bar/baz',
    {
        'test':     (True, True, False, False, True, True),
        'validate': (True, True, False, False)
}), (
# 53
    '*/bar/**',
    'foo/bar/baz/x',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 54
    '*/bar/**',
    'deep/foo/bar/baz/x',
    {
        'test':     (True, True, False, False, False, False),
        'validate': (True, True, False, False)
}), (
# 55
    '**/bar/*/*',
    'deep/foo/bar/baz/x',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# VARIOUS ADDITIONAL
# 56
    'a[c-c]st',
    'acrt',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 57
    'a[c-c]rt',
    'acrt',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 58
    '[!]-]',
    ']',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 59
    '[!]-]',
    'a',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 60
    '\\',
    '',
    {
        'test':     ('CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError'),
        'validate': (False, False, False, False)
}), (
# 61
    '\\',
    '\\',
    {
        'test':     ('CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError'),
        'validate': (False, False, False, False)
}), (
# 62
    '*/\\',
    'XXX/\\',
    {
        'test':     ('CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError'),
        'validate': (False, False, False, False)
}), (
# 63
    '*/\\\\',
    'XXX/\\',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 64
    'foo',
    'foo',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 65
    '@foo',
    '@foo',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 66
    '@foo',
    'foo',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 67
    '\\[ab]',
    '[ab]',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 68
    '[[]ab]',
    '[ab]',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 69
    '[[:]ab]',
    '[ab]',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 70
    '[[::]ab]',
    '[ab]',
    {
        'test':     (True, True, True, True, True, True), #XXX diff ok
        'validate': (False, False, False, False)
}), (
# 71
    '[[:digit]ab]',
    '[ab]',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 72
    '[\\[:]ab]',
    '[ab]',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 73
    '\\??\\?b',
    '?a?b',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 74
    '\\a\\b\\c',
    'abc',
    {
        'test':     ('CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError'),
        'validate': (True, True, True, True)
}), (
# 75
    '',
    'foo',
    {
        'test':     ('PatternArgumentError', 'PatternArgumentError', 'PatternArgumentError', 'PatternArgumentError', 'PatternArgumentError', 'PatternArgumentError'),
        'validate': (False, False, False, False)
}), (
# 76
    '**/t[o]',
    'foo/bar/baz/to',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# CHARACTER CLASSES
# 77
    '[[:alpha:]][[:digit:]][[:upper:]]',
    'a1B',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 78
    '[[:digit:][:upper:][:space:]]',
    'a',
    {
        'test':     (False, True, False, True, False, True),
        'validate': (False, True, False, True)
}), (
# 79
    '[[:digit:][:upper:][:space:]]',
    'A',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 80
    '[[:digit:][:upper:][:space:]]',
    '1',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 81
    '[[:digit:][:upper:][:spaci:]]',
    '1',
    {
        'test':     ('CharacterClassNameError', 'CharacterClassNameError', 'CharacterClassNameError', 'CharacterClassNameError', 'CharacterClassNameError', 'CharacterClassNameError'),
        'validate': (False, False, False, False)
}), (
# 82
    '[[:digit:][:upper:][:space:]]',
    ' ',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 83
    '[[:digit:][:upper:][:space:]]',
    '.',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 84
    '[[:digit:][:punct:][:space:]]',
    '.',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 85
    '[[:xdigit:]]',
    '5',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 86
    '[[:xdigit:]]',
    'f',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 87
    '[[:xdigit:]]',
    'D',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 88
    '[[:alnum:][:alpha:][:blank:][:cntrl:][:digit:][:graph:][:lower:][:print:][:punct:][:space:][:upper:][:xdigit:]]',
    '_',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 89
    '[^[:alnum:][:alpha:][:blank:][:cntrl:][:digit:][:lower:][:space:][:upper:][:xdigit:]]',
    '.',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 90
    '[a-c[:digit:]x-z]',
    '5',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 91
    '[a-c[:digit:]x-z]',
    'b',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 92
    '[a-c[:digit:]x-z]',
    'y',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 93
    '[a-c[:digit:]x-z]',
    'q',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# ADDITIONAL WITH MALFORMED
# 94
    '[\\\\-^]',
    ']',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 95
    '[\\\\-^]',
    '[',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 96
    '[\\-_]',
    '-',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 97
    '[\\]]',
    ']',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 98
    '[\\]]',
    '\\]',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 99
    '[\\]]',
    '\\',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 100
    'a[]b',
    'ab',
    {
        'test':     ('EmptyCharacterSetError', 'EmptyCharacterSetError', 'EmptyCharacterSetError', 'EmptyCharacterSetError', 'EmptyCharacterSetError', 'EmptyCharacterSetError'),
        'validate': (False, False, False, False)
}), (
# 101
    'a[]b',
    'a[]b',
    {
        'test':     ('EmptyCharacterSetError', 'EmptyCharacterSetError', 'EmptyCharacterSetError', 'EmptyCharacterSetError', 'EmptyCharacterSetError', 'EmptyCharacterSetError'),
        'validate': (False, False, False, False)
}), (
# 102
    'ab[',
    'ab[',
    {
        'test':     (True, True, True, True, True, True), #XXX diff ok
        'validate': (False, False, False, False)
}), (
# 103
    '[!',
    'ab',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 104
    '[-',
    'ab',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 105
    '[-]',
    '-',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 106
    '[a-',
    '-',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 107
    '[!a-',
    '-',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 108
    '[--A]',
    '-',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 109
    '[--A]',
    '5',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 110
    '[ --]',
    ' ',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 111
    '[ --]',
    '$',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 112
    '[ --]',
    '-',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 113
    '[ --]',
    '0',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 114
    '[---]',
    '-',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 115
    '[------]',
    '-',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 116
    '[a-e-n]',
    'j',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 117
    '[a-e-n]',
    '-',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 118
    '[!------]',
    'a',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 119
    '[]-a]',
    '[',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 120
    '[]-a]',
    '^',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 121
    '[!]-a]',
    '^',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 122
    '[!]-a]',
    '[',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 123
    '[a^bc]',
    '^',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 124
    '[a-]b]',
    '-b]',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 125
    '[\\]',
    '\\',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 126
    '[\\\\]',
    '\\',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 127
    '[!\\\\]',
    '\\',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 128
    '[A-\\\\]',
    'G',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 129
    'b*a',
    'aaabbb',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 130
    '*ba*',
    'aabcaa',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 131
    '[,]',
    ',',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 132
    '[\\\\,]',
    ',',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 133
    '[\\\\,]',
    '\\',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 134
    '[,-.]',
    '-',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 135
    '[,-.]',
    '+',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 136
    '[,-.]',
    '-.]',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 137
    '[\\1-\\3]',
    '2',
    {
        'test':     (False, False, False, False, False, False), #XXX diff ok
        'validate': (True, True, True, True)
}), (
# 138
    '[\\1-\\3]',
    '3',
    {
        'test':     (False, False, False, False, False, False), #XXX diff ok
        'validate': (True, True, True, True)
}), (
# 139
    '[\\1-\\3]',
    '4',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 140
    '[[-\\]]',
    '\\',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 141
    '[[-\\]]',
    '[',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 142
    '[[-\\]]',
    ']',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 143
    '[[-\\]]',
    '-',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# RECURSION
# 144
    '-*-*-*-*-*-*-12-*-*-*-m-*-*-*',
    '-adobe-courier-bold-o-normal--12-120-75-75-m-70-iso8859-1',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 145
    '-*-*-*-*-*-*-12-*-*-*-m-*-*-*',
    '-adobe-courier-bold-o-normal--12-120-75-75-X-70-iso8859-1',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 146
    '-*-*-*-*-*-*-12-*-*-*-m-*-*-*',
    '-adobe-courier-bold-o-normal--12-120-75-75-/-70-iso8859-1',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 147
    'XXX/*/*/*/*/*/*/12/*/*/*/m/*/*/*',
    'XXX/adobe/courier/bold/o/normal//12/120/75/75/m/70/iso8859/1',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 148
    'XXX/*/*/*/*/*/*/12/*/*/*/m/*/*/*',
    'XXX/adobe/courier/bold/o/normal//12/120/75/75/X/70/iso8859/1',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 149
    '**/*a*b*g*n*t',
    'abcd/abcdefg/abcdefghijk/abcdefghijklmnop.txt',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 150
    '**/*a*b*g*n*t',
    'abcd/abcdefg/abcdefghijk/abcdefghijklmnop.txtz',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 151
    '*/*/*',
    'foo',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 152
    '*/*/*',
    'foo/bar',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 153
    '*/*/*',
    'foo/bba/arr',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 154
    '*/*/*',
    'foo/bb/aa/rr',
    {
        'test':     (True, True, False, False, False, False),
        'validate': (True, True, False, False)
}), (
# 155
    '**/**/**',
    'foo/bb/aa/rr',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 156
    '*X*i',
    'abcXdefXghi',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 157
    '*X*i',
    'ab/cXd/efXg/hi',
    {
        'test':     (True, True, False, False, False, False),
        'validate': (True, True, False, False)
}), (
# 158
    '*/*X*/*/*i',
    'ab/cXd/efXg/hi',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 159
    '**/*X*/**/*i',
    'ab/cXd/efXg/hi',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# PATHMATCH
# 160
    'fo',
    'foo',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 161
    'foo/bar',
    'foo/bar',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 162
    'foo/*',
    'foo/bar',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 163
    'foo/*',
    'foo/bba/arr',
    {
        'test':     (True, True, False, False, False, False),
        'validate': (True, True, False, False)
}), (
# 164
    'foo/**',
    'foo/bba/arr',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 165
    'foo*',
    'foo/bba/arr',
    {
        'test':     (True, True, False, False, False, False),
        'validate': (True, True, False, False)
}), (
# 166
    'foo**',
    'foo/bba/arr',
    {
        'test':     (True, True, False, False, True, True),
        'validate': (True, True, False, False)
}), (
# 167
    'foo/*arr',
    'foo/bba/arr',
    {
        'test':     (True, True, False, False, False, False),
        'validate': (True, True, False, False)
}), (
# 168
    'foo/**arr',
    'foo/bba/arr',
    {
        'test':     (True, True, False, False, True, True),
        'validate': (True, True, False, False)
}), (
# 169
    'foo/*z',
    'foo/bba/arr',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 170
    'foo/**z',
    'foo/bba/arr',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False, False, False)
}), (
# 171
    '*Xg*i',
    'ab/cXd/efXg/hi',
    {
        'test':     (True, True, False, False, False, False),
        'validate': (True, True, False, False)
}), (
# CASE SENSITIVITY
# 172
    '[A-Z]',
    'a',
    {
        'test':     (False, True, False, True, False, True),
        'validate': (False, True, False, True)
}), (
# 173
    '[A-Z]',
    'A',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 174
    '[a-z]',
    'A',
    {
        'test':     (False, True, False, True, False, True),
        'validate': (False, True, False, True)
}), (
# 175
    '[a-z]',
    'a',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 176
    '[[:upper:]]',
    'a',
    {
        'test':     (False, True, False, True, False, True),
        'validate': (False, True, False, True)
}), (
# 177
    '[[:upper:]]',
    'A',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 178
    '[[:lower:]]',
    'A',
    {
        'test':     (False, True, False, True, False, True),
        'validate': (False, True, False, True)
}), (
# 179
    '[[:lower:]]',
    'a',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 180
    '[B-Za]',
    'A',
    {
        'test':     (False, True, False, True, False, True),
        'validate': (False, True, False, True)
}), (
# 181
    '[B-Za]',
    'a',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 182
    '[B-a]',
    'A',
    {
        'test':     (False, True, False, True, False, True),
        'validate': (False, True, False, True)
}), (
# 183
    '[B-a]',
    'a',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}), (
# 184
    '[Z-y]',
    'z',
    {
        'test':     (False, True, False, True, False, True),
        'validate': (False, True, False, True)
}), (
# 188
    '[Z-y]',
    'Z',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True, True, True)
}))

