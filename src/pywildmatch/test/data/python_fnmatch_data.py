# cpython/Lib/test/test_fnmatch.py
# TEST CASES FOR fnmatch MODULE

# DATA = (
#     '<PATTERN>', '<TEXT>', {<RESULTS>},
# ),

DATA = ((
    'abc', 'abc', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '?*?', 'abc', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '???*', 'abc', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '*???', 'abc', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '???', 'abc', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '*', 'abc', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'ab[cd]', 'abc', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'ab[!de]', 'abc', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'ab[de]', 'abc', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '??', 'a', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    'b', 'a', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
# these test that '\' is handled correctly in character sets;
# see SF bug #409651
    r'[\]', '\\', {
        'python_fnmatch': (1, 1),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    r'[!\]', 'a', {
        'python_fnmatch': (1, 1),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    r'[!\]', '\\', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
# test that filenames with newlines in them are handled correctly.
# http://bugs.python.org/issue6665
    'foo*', 'foo\nbar', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'foo*', 'foo\nbar\n', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'foo*', '\nfoo', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '*', '\n', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
# test_mix_bytes_str
# TypeError
    b'*', 'pathname', {
        'python_fnmatch': (1, 1), # sre_match because arg handling
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '*', b'pathname', {
        'python_fnmatch': (1, 1), # sre_match because arg handling
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
# test_fnmatchcase
    'abc', 'AbC', {
        'python_fnmatch': (0, 1),
        'libgit2': (0, 1, 0, 1),
        'pywildmatch': (0, 1, 0, 1, 0, 1)
}), (
    'AbC', 'abc', {
        'python_fnmatch': (0, 1),
        'libgit2': (0, 1, 0, 1),
        'pywildmatch': (0, 1, 0, 1, 0, 1)
}), (
# test_bytes
    b'te*', b'test', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    b'te*\xff', b'test\xff', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    b'foo*', b'foo\nbar', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
# test_translate
    '*', 'pathname', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '?', '.', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'a?b*', 'a9b9_', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[abc]', 'a', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[]]', ']', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[!x]', 'x', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[^x]', ':', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[x', '[x', {
        'python_fnmatch': (1, 1),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}))


if __name__ == '__main__':
    from __init__ import validate_data
    for dataset in DATA:
        validate_data(dataset),
    print(__file__, len(DATA), 'tests'),


