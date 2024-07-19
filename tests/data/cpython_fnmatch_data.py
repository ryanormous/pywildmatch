
# BASED ON TEST CASES FOR cpython fnmatch MODULE
# cpython/Lib/test/test_fnmatch.py
# VERSION: v3.13.0a3-347


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# DATA

DATA = ((
# fnmatch
# 0
    'abc',
    'abc',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 1
    '?*?',
    'abc',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 2
    '???*',
    'abc',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 3
    '*???',
    'abc',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 4
    '???',
    'abc',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 5
    '*',
    'abc',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 6
    'ab[cd]',
    'abc',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 7
    'ab[!de]',
    'abc',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 8
    'ab[de]',
    'abc',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 9
    '??',
    'a',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 10
    'b',
    'a',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# fnmatch — HANDLE '\'  IN CHARACTER SETS
# WHAT IS "SF bug #409651"?  SEE: LINK?
# 11
    r'[\]',
    '\\',
    {
        'test':     (False, False, False, False, False, False), #XXX diff ok
        'validate': (True, True)
}), (
# 12
    r'[!\]',
    'a',
    {
        'test':     (False, False, False, False, False, False), #XXX diff ok
        'validate': (True, True)
}), (
# 13
    r'[!\]',
    '\\',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# fnmatch — HANDLE NEWLINES
# SEE: https://bugs.python.org/issue6665
# 14
    'foo*',
    'foo\nbar',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 15
    'foo*',
    'foo\nbar\n',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 16
    'foo*',
    '\nfoo',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 17
    '*',
    '\n',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# SLOW fnmatch
# 18
    '*a*a*a*a*a*a*a*a*a*a',
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 19
    # SEE: https://bugs.python.org/issue40480
    '*a*a*a*a*a*a*a*a*a*a',
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# MIX bytes AND str TYPE
# 20
    b'*',
    'test',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 21
    '*',
    b'test',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 22
    b'*',
    'test',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 23
    '*',
    b'test',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# fnmatchcase
# 24
    'abc',
    'AbC',
    {
        'test':     (False, True, False, True, False, True),
        'validate': (False, True)
}), (
# 25
    'AbC',
    'abc',
    {
        'test':     (False, True, False, True, False, True),
        'validate': (False, True)
}), (
# 26
    'AbC',
    'AbC',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 27
    'usr/bin',
    'usr/bin',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 28
    'usr/bin',
    'usr\\bin',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 29
    'usr\\bin',
    'usr/bin',
    {
        'test':     ('CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError'), #XXX diff ok
        'validate': (False, False)
}), (
# 30
    'usr\\bin',
    'usr\\bin',
    {
        'test':     ('CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError'), #XXX diff ok
        'validate': (True, True)
}), (
# BYTES TYPE
# 31
    b'te*',
    b'test',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 32
    b'te*\xff',
    b'test\xff',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 33
    b'foo*',
    b'foo\nbar',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# CHARACTER SET
# 34
    '[az]',
    'a',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[az]',
    '`',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[az]',
    'z',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[az]',
    '{',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 35
    '[!az]',
    'a',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[!az]',
    '`',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[!az]',
    'z',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[!az]',
    '{',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# CHARACTER SET — CASE INSENSITIVE
# 36
    '[AZ]',
    'a',
    {
        'test':     (False, True, False, True, False, True),
        'validate': (False, True)
}), (
    '[AZ]',
    '@',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[AZ]',
    'z',
    {
        'test':     (False, True, False, True, False, True),
        'validate': (False, True)
}), (
    '[AZ]',
    '[',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 37
    '[!AZ]',
    'a',
    {
        'test':     (True, False, True, False, True, False),
        'validate': (True, False)
}), (
    '[!AZ]',
    '@',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[!AZ]',
    'z',
    {
        'test':     (True, False, True, False, True, False),
        'validate': (True, False)
}), (
    '[!AZ]',
    '[',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 38
    '[az]',
    'A',
    {
        'test':     (False, True, False, True, False, True),
        'validate': (False, True)
}), (
    '[az]',
    '`',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[az]',
    'Z',
    {
        'test':     (False, True, False, True, False, True),
        'validate': (False, True)
}), (
    '[az]',
    '{',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 39
    '[!az]',
    'A',
    {
        'test':     (True, False, True, False, True, False),
        'validate': (True, False)
}), (
    '[!az]',
    '`',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[!az]',
    'Z',
    {
        'test':     (True, False, True, False, True, False),
        'validate': (True, False)
}), (
    '[!az]',
    '{',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# CHARACTER SET — REPEATED SAME CHARACTER
# 40
    '[aa]',
    '`',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[aa]',
    'a',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[!aa]',
    'a',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[!aa]',
    '`',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# CHARACTER SET — SPECIAL CASES
# 41
    '[^az]',
    '^',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[^az]',
    '`',
    {
        'test':     (True, True, True, True, True, True), #XXX diff ok
        'validate': (False, False)
}), (
    '[^az]',
    'a',
    {
        'test':     (False, False, False, False, False, False), #XXX diff ok
        'validate': (True, True)
}), (
    '[^az]',
    '{',
    {
        'test':     (True, True, True, True, True, True), #XXX diff ok
        'validate': (False, False)
}), (
# 42
    '[[az]',
    '[',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[[az]',
    '`',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[[az]',
    'a',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[[az]',
    '{',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 43 
    r'[!]]',
    'Z',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    r'[!]]',
    '[',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    r'[!]]',
    ']',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    r'[!]]',
    'a',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 44
    '[',
    '[',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 45
    '[]',
    '[]',
    {
        'test':     ('EmptyCharacterSetError', 'EmptyCharacterSetError', 'EmptyCharacterSetError', 'EmptyCharacterSetError', 'EmptyCharacterSetError', 'EmptyCharacterSetError'),
        'validate': (True, True)
}), (
# 46
    '[!',
    '[!',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 47
    '[!]',
    '[!]',
    {
        'test':     ('EmptyCharacterSetError', 'EmptyCharacterSetError', 'EmptyCharacterSetError', 'EmptyCharacterSetError', 'EmptyCharacterSetError', 'EmptyCharacterSetError'),
        'validate': (True, True)
}), (
# CHARACTER SET RANGE
# 48
    '[b-d]',
    'a',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[b-d]',
    'c',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[b-d]',
    'd',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[b-d]',
    'e',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 49
    '[!b-d]',
    'a',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[!b-d]',
    'c',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[!b-d]',
    'd',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[!b-d]',
    'e',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 50
    '[b-dx-z]',
    'w',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[b-dx-z]',
    'x',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[b-dx-z]',
    'y',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[b-dx-z]',
    '{',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 51
    '[!b-dx-z]',
    'w',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[!b-dx-z]',
    'x',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[!b-dx-z]',
    'y',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[!b-dx-z]',
    '{',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# CHARACTER SET RANGE — CASE INSENSITIVE
# 52
    '[B-D]',
    'a',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[B-D]',
    'c',
    {
        'test':     (False, True, False, True, False, True),
        'validate': (False, True)
}), (
    '[B-D]',
    'd',
    {
        'test':     (False, True, False, True, False, True),
        'validate': (False, True)
}), (
    '[B-D]',
    'e',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 53
    '[!B-D]',
    'a',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[!B-D]',
    'c',
    {
        'test':     (True, False, True, False, True, False),
        'validate': (True, False)
}), (
    '[!B-D]',
    'd',
    {
        'test':     (True, False, True, False, True, False),
        'validate': (True, False)
}), (
    '[!B-D]',
    'e',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 54
    '[b-d]',
    'A',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[b-d]',
    'C',
    {
        'test':     (False, True, False, True, False, True),
        'validate': (False, True)
}), (
    '[b-d]',
    'D',
    {
        'test':     (False, True, False, True, False, True),
        'validate': (False, True)
}), (
    '[b-d]',
    'E',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 55
    '[!b-d]',
    'A',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[!b-d]',
    'C',
    {
        'test':     (True, False, True, False, True, False),
        'validate': (True, False)
}), (
    '[!b-d]',
    'D',
    {
        'test':     (True, False, True, False, True, False),
        'validate': (True, False)
}), (
    '[!b-d]',
    'E',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# CHARACTER SET RANGE — UPPER BOUND EQUALS LOWER BOUND
# 56
    '[b-b]',
    'B',
    {
        'test':     (False, True, False, True, False, True),
        'validate': (False, True)
}), (
    '[b-b]',
    'a',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[b-b]',
    'b',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[b-b]',
    'c',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# CHARACTER SET RANGE — SPECIAL CASES
# 57
    '[!-#]',
    '"',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[!-#]',
    '#',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[!-#]',
    ',',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[!-#]',
    '-',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 58
    '[!--.]',
    ',',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[!--.]',
    '-',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[!--.]',
    '.',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[!--.]',
    '0',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 59
    '[^-`]',
    ']',
    {
        'test':     (True, True, True, True, True, True), #XXX diff ok
        'validate': (False, False)
}), (
    '[^-`]',
    '^',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[^-`]',
    '_',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[^-`]',
    'a',
    {
        'test':     (True, True, True, True, True, True), #XXX diff ok
        'validate': (False, False)
}), (
# CHARACTER SET RANGE — NORMALIZED PATH SEPERATOR
# 60
    '[[-^]',
    'Z',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[[-^]',
    '[',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[[-^]',
    '^',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[[-^]',
    '_',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 61 
    r'[\-^]',
    '[',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    r'[\-^]',
    '\\',
    {
        'test':     (False, False, False, False, False, False), #XXX diff ok
        'validate': (True, True)
}), (
    r'[\-^]',
    ']',
    {
        'test':     (False, False, False, False, False, False), #XXX diff ok
        'validate': (True, True)
}), (
    r'[\-^]',
    '_',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# CHARACTER SET RANGE — SPECIAL CASES
# 62
    '[b-]',
    ',',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[b-]',
    '-',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[b-]',
    'a',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[b-]',
    'b',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 63
    '[!b-]',
    ',',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[!b-]',
    '-',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[!b-]',
    'a',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[!b-]',
    'b',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 64
    '[-b]',
    ',',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[-b]',
    '-',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[-b]',
    'a',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[-b]',
    'b',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 65
    '[!-b]',
    ',',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[!-b]',
    '-',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[!-b]',
    'a',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[!-b]',
    'b',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 66
    '[-]',
    ',',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[-]',
    '-',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[-]',
    'Z',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[-]',
    '[',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 67
    '[!-]',
    ',',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[!-]',
    '-',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[!-]',
    'Z',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[!-]',
    '[',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# CHARACTER SET RANGE — UPPER BOUND LESS THAN LOWER BOUND
# 68
    '[d-b]',
    'a',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[d-b]',
    'b',
    {
        'test':     (True, True, True, True, True, True), #XXX diff ok
        'validate': (False, False)
}), (
    '[d-b]',
    'c',
    {
        'test':     (True, True, True, True, True, True), #XXX diff ok
        'validate': (False, False)
}), (
    '[d-b]',
    'd',
    {
        'test':     (True, True, True, True, True, True), #XXX diff ok
        'validate': (False, False)
}), (
# 69
    '[!d-b]',
    'a',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[!d-b]',
    'b',
    {
        'test':     (False, False, False, False, False, False), #XXX diff ok
        'validate': (True, True)
}), (
    '[!d-b]',
    'c',
    {
        'test':     (False, False, False, False, False, False), #XXX diff ok
        'validate': (True, True)
}), (
    '[!d-b]',
    'd',
    {
        'test':     (False, False, False, False, False, False), #XXX diff ok
        'validate': (True, True)
}), (
# 70
    '[d-bx-z]',
    'c',
    {
        'test':     (True, True, True, True, True, True), #XXX diff ok
        'validate': (False, False)
}), (
    '[d-bx-z]',
    'd',
    {
        'test':     (True, True, True, True, True, True), #XXX diff ok
        'validate': (False, False)
}), (
    '[d-bx-z]',
    'w',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
    '[d-bx-z]',
    'x',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 71
    '[!d-bx-z]',
    'c',
    {
        'test':     (False, False, False, False, False, False), #XXX diff ok
        'validate': (True, True)
}), (
    '[!d-bx-z]',
    'd',
    {
        'test':     (False, False, False, False, False, False), #XXX diff ok
        'validate': (True, True)
}), (
    '[!d-bx-z]',
    'w',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[!d-bx-z]',
    'x',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 72
    '[d-b^-`]',
    'c',
    {
        'test':     (True, True, True, True, True, True), #XXX diff ok
        'validate': (False, False)
}), (
    '[d-b^-`]',
    'd',
    {
        'test':     (True, True, True, True, True, True), #XXX diff ok
        'validate': (False, False)
}), (
    '[d-b^-`]',
    '_',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[d-b^-`]',
    '`',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 73
    '[d-b[-^]',
    'c',
    {
        'test':     (True, True, True, True, True, True), #XXX diff ok
        'validate': (False, False)
}), (
    '[d-b[-^]',
    'd',
    {
        'test':     (True, True, True, True, True, True), #XXX diff ok
        'validate': (False, False)
}), (
    '[d-b[-^]',
    '[',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
    '[d-b[-^]',
    '^',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# CHARACTER SET — PATH SEPERATOR IN CHARACTER SET
# 74
    '[/]',
    '/',
    {
        'test':     (True, True, 'EmptyCharacterSetError', 'EmptyCharacterSetError', True, True),
        'validate': (True, True)
}), (
# 75
    r'[\]',
    '\\',
    {
        'test':     (False, False, False, False, False, False), #XXX diff ok
        'validate': (True, True)
}), (
# 76
    r'[\]',
    '/',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 77
    '[/]',
    '\\',
    {
        'test':     (False, False, 'EmptyCharacterSetError', 'EmptyCharacterSetError', False, False),
        'validate': (False, False)
}), (
# 78
    '[/]',
    '[/]',
    {
        'test':     (False, False, 'EmptyCharacterSetError', 'EmptyCharacterSetError', False, False),
        'validate': (False, False)
}), (
# 79
    '[/]',
    r'[\\]',
    {
        'test':     (False, False, 'EmptyCharacterSetError', 'EmptyCharacterSetError', False, False),
        'validate': (False, False)
}), (
# 80
    r'[\t]',
    '\\',
    {
        'test':     (False, False, False, False, False, False), #XXX diff ok
        'validate': (True, True)
}), (
# 81
    r'[\t]',
    '/',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 82
    r'[\t]',
    't',
    {
        'test':     (False, False, False, False, False, False), #XXX diff ok
        'validate': (True, True)
}), (
# 83
    r'[\t]',
    '\t',
    {
        'test':     (True, True, True, True, True, True), #XXX diff ok
        'validate': (False, False)
}), (
# CHARACTER SET RANGE — PATH SEPERATOR
# 84
    'a[.-0]b',
    'a/b',
    {
        'test':     (True, True, False, False, True, True),
        'validate': (True, True)
}), (
# 85
    'a[.-0]b',
    'a\\b',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 86
    'a[Z-^]b',
    r'a\\b',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 87
    'a[Z-^]b',
    'a/b',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 88
    'a[/-0]b',
    'a/b',
    {
        'test':     (True, True, False, False, True, True),
        'validate': (True, True)
}), (
# 89
    'a[/-0]b',
    r'a\b',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 90
    'a[/-0]b',
    'a[/-0]b',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 91
    'a[/-0]b',
    r'a[\-0]b',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 92
    'a[.-/]b',
    'a/b',
    {
        'test':     (True, True, False, False, True, True),
        'validate': (True, True)
}), (
# 93
    'a[.-/]b',
    r'a\b',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 94
    'a[.-/]b',
    'a[.-/]b',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 95
    'a[.-/]b',
    r'a[.-\]b',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 96
    r'a[\-^]b',
    r'a\b',
    {
        'test':     (False, False, False, False, False, False), #XXX diff ok
        'validate': (True, True)
}), (
# 97
    r'a[\-^]b',
    'a/b',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 98
    r'a[\-^]b',
    r'a[\-^]b',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 99
    r'a[\-^]b',
    'a[/-^]b',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 100
    r'a[Z-\]b',
    r'a\b',
    {
        'test':     (False, False, False, False, False, False), #XXX diff ok
        'validate': (True, True)
}), (
# 101
    r'a[Z-\]b',
    'a/b',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 102
    r'a[Z-\]b',
    r'a[Z-\]b',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 103
    r'a[Z-\]b',
    'a[Z-/]b',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# FutureWarning
# SEE: https://unicode.org/reports/tr18/#RL1.3
# 104
    '[[]',
    '[',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 105
    '[a&&b]',
    '&',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 106
    '[a||b]',
    '|',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 107
    '[a~~b]',
    '~',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 108
    '[a-z+--A-Z]',
    ',',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 109
    '[a-z--/A-Z]',
    '.',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}))

