# DATA = (
#     '<PATTERN>', '<TEXT>', {<RESULTS>}
# ),

DATA = ((
    'foo', 'foo', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'bar', 'foo', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '', '', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '???', 'foo', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '??', 'foo', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '*', 'foo', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'f*', 'foo', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '*f', 'foo', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '*foo*', 'foo', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '*ob*a*r*', 'foobar', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '*ab', 'aaaaaaabababab', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'foo\\*', 'foo*', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'foo\\*bar', 'foobar', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    'f\\\\oo', 'f\\oo', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '*[al]?', 'ball', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[ten]', 'ten', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '**[!te]', 'ten', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '**[!ten]', 'ten', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    't[a-g]n', 'ten', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    't[!a-g]n', 'ten', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    't[!a-g]n', 'ton', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    't[^a-g]n', 'ton', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'a[]]b', 'a]b', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    'a[]-]b', 'a-b', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    'a[]-]b', 'a]b', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    'a[]-]b', 'aab', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    'a[]a-]b', 'aab', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    ']', ']', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'foo*bar', 'foo/baz/bar', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 0, 0),
        'pywildmatch': (1, 1, 0, 0, 0, 0)
}), (
    'foo**bar', 'foo/baz/bar', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 0, 0),
        'pywildmatch': (1, 1, 0, 0, 1, 1)
}), (
    'foo**bar', 'foobazbar', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'foo/**/bar', 'foo/baz/bar', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'foo/**/**/bar', 'foo/baz/bar', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 1, 1),
        'pywildmatch': (0,0, 1, 1, 0, 0)
}), (
    'foo/**/bar', 'foo/b/a/z/bar', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'foo/**/**/bar', 'foo/b/a/z/bar', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'foo/**/bar', 'foo/bar', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 1, 1),
        'pywildmatch': (0, 0, 1, 1, 0, 0)
}), (
    'foo/**/**/bar', 'foo/bar', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 1, 1),
        'pywildmatch': (0, 0, 1, 1, 0, 0)
}), (
# DUPLICATE: 'foo?bar', 'foo/bar'
# DUPLICATE: 'foo[/]bar', 'foo/bar'
    'foo[^a-z]bar', 'foo/bar', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 0, 0),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'f[^eiu][^eiu][^eiu][^eiu][^eiu]r', 'foo/bar', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 0, 0),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'f[^eiu][^eiu][^eiu][^eiu][^eiu]r', 'foo-bar', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '**/foo', 'foo', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 1, 1),
        'pywildmatch': (0, 0, 1, 1, 0, 0)
}), (
    '**/foo', 'XXX/foo', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '**/foo', 'bar/baz/foo', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '*/foo', 'bar/baz/foo', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 0, 0),
        'pywildmatch': (1, 1, 0, 0, 0, 0)
}), (
    '**/bar*', 'foo/bar/baz', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 0, 0),
        'pywildmatch': (1, 1, 0, 0, 0, 0)
}), (
    '**/bar/*', 'deep/foo/bar/baz', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '**/bar/*', 'deep/foo/bar/baz/', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 0, 0),
        'pywildmatch': (1, 1, 0, 0, 0, 0)
}), (
    '**/bar/**', 'deep/foo/bar/baz/', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '**/bar/*', 'deep/foo/bar', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '**/bar/**', 'deep/foo/bar/', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '**/bar**', 'foo/bar/baz', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 0, 0),
        'pywildmatch': (1, 1, 0, 0, 1, 1)
}), (
    '*/bar/**', 'foo/bar/baz/x', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '*/bar/**', 'deep/foo/bar/baz/x', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 0, 0),
        'pywildmatch': (1, 1, 0, 0, 0, 0)
}), (
    '**/bar/*/*', 'deep/foo/bar/baz/x', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'a[c-c]st', 'acrt', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    'a[c-c]rt', 'acrt', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[!]-]', ']', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[!]-]', 'a', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '\\', '', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '\\', '\\', {
        'python_fnmatch': (1, 1),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '*/\\', 'XXX/\\', {
        'python_fnmatch': (1, 1),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '*/\\\\', 'XXX/\\', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'foo', 'foo', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '@foo', '@foo', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '@foo', 'foo', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '\\[ab]', '[ab]', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[[]ab]', '[ab]', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[[:]ab]', '[ab]', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[[::]ab]', '[ab]', {
        'python_fnmatch': (1, 1),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[[:digit]ab]', '[ab]', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[\\[:]ab]', '[ab]', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '\\??\\?b', '?a?b', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '\\a\\b\\c', 'abc', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '', 'foo', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '**/t[o]', 'foo/bar/baz/to', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[[:alpha:]][[:digit:]][[:upper:]]', 'a1B', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[[:digit:][:upper:][:space:]]', 'a', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 1, 0, 1),
        'pywildmatch': (0, 1, 0, 1, 0, 1)
}), (
    '[[:digit:][:upper:][:space:]]', 'A', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[[:digit:][:upper:][:space:]]', '1', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[[:digit:][:upper:][:spaci:]]', '1', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[[:digit:][:upper:][:space:]]', ' ', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[[:digit:][:upper:][:space:]]', '.', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[[:digit:][:punct:][:space:]]', '.', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[[:xdigit:]]', '5', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[[:xdigit:]]', 'f', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[[:xdigit:]]', 'D', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[[:alnum:][:alpha:][:blank:][:cntrl:][:digit:][:graph:][:lower:][:print:][:punct:][:space:][:upper:][:xdigit:]]', '_', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[^[:alnum:][:alpha:][:blank:][:cntrl:][:digit:][:lower:][:space:][:upper:][:xdigit:]]', '.', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[a-c[:digit:]x-z]', '5', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[a-c[:digit:]x-z]', 'b', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[a-c[:digit:]x-z]', 'y', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[a-c[:digit:]x-z]', 'q', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[\\\\-^]', ']', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[\\\\-^]', '[', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[\\-_]', '-', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[\\]]', ']', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[\\]]', '\\]', {
        'python_fnmatch': (1, 1),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[\\]]', '\\', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    'a[]b', 'ab', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    'a[]b', 'a[]b', {
        'python_fnmatch': (1, 1),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    'ab[', 'ab[', {
        'python_fnmatch': (1, 1),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[!', 'ab', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[-', 'ab', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[-]', '-', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[a-', '-', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[!a-', '-', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[--A]', '-', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[--A]', '5', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[ --]', ' ', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[ --]', '$', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[ --]', '-', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[ --]', '0', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[---]', '-', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[------]', '-', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[a-e-n]', 'j', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[a-e-n]', '-', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[!------]', 'a', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[]-a]', '[', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[]-a]', '^', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[!]-a]', '^', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[!]-a]', '[', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[a^bc]', '^', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[a-]b]', '-b]', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[\\]', '\\', {
        'python_fnmatch': (1, 1),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[\\\\]', '\\', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[!\\\\]', '\\', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[A-\\\\]', 'G', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'b*a', 'aaabbb', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '*ba*', 'aabcaa', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[,]', ',', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[\\\\,]', ',', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[\\\\,]', '\\', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[,-.]', '-', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[,-.]', '+', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[,-.]', '-.]', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[\\1-\\3]', '2', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[\\1-\\3]', '3', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[\\1-\\3]', '4', {
        'python_fnmatch': (1, 1),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[[-\\]]', '\\', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[[-\\]]', '[', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[[-\\]]', ']', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '[[-\\]]', '-', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '-*-*-*-*-*-*-12-*-*-*-m-*-*-*', '-adobe-courier-bold-o-normal--12-120-75-75-m-70-iso8859-1', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '-*-*-*-*-*-*-12-*-*-*-m-*-*-*', '-adobe-courier-bold-o-normal--12-120-75-75-X-70-iso8859-1', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '-*-*-*-*-*-*-12-*-*-*-m-*-*-*', '-adobe-courier-bold-o-normal--12-120-75-75-/-70-iso8859-1', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    'XXX/*/*/*/*/*/*/12/*/*/*/m/*/*/*', 'XXX/adobe/courier/bold/o/normal//12/120/75/75/m/70/iso8859/1', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'XXX/*/*/*/*/*/*/12/*/*/*/m/*/*/*', 'XXX/adobe/courier/bold/o/normal//12/120/75/75/X/70/iso8859/1', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '**/*a*b*g*n*t', 'abcd/abcdefg/abcdefghijk/abcdefghijklmnop.txt', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '**/*a*b*g*n*t', 'abcd/abcdefg/abcdefghijk/abcdefghijklmnop.txtz', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '*/*/*', 'foo', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '*/*/*', 'foo/bar', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    '*/*/*', 'foo/bba/arr', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '*/*/*', 'foo/bb/aa/rr', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 0, 0),
        'pywildmatch': (1, 1, 0, 0, 0, 0)
}), (
    '**/**/**', 'foo/bb/aa/rr', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '*X*i', 'abcXdefXghi', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '*X*i', 'ab/cXd/efXg/hi', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 0, 0),
        'pywildmatch': (1, 1, 0, 0, 0, 0)
}), (
    '*/*X*/*/*i', 'ab/cXd/efXg/hi', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '**/*X*/**/*i', 'ab/cXd/efXg/hi', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'fo', 'foo', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    'foo/bar', 'foo/bar', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'foo/*', 'foo/bar', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'foo/*', 'foo/bba/arr', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 0, 0),
        'pywildmatch': (1, 1, 0, 0, 0, 0)
}), (
    'foo/**', 'foo/bba/arr', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'foo*', 'foo/bba/arr', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 0, 0),
        'pywildmatch': (1, 1, 0, 0, 0, 0)
}), (
    'foo**', 'foo/bba/arr', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 0, 0),
        'pywildmatch': (1, 1, 0, 0, 1, 1)
}), (
    'foo/*arr', 'foo/bba/arr', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 0, 0),
        'pywildmatch': (1, 1, 0, 0, 0, 0)
}), (
    'foo/**arr', 'foo/bba/arr', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 0, 0),
        'pywildmatch': (1, 1, 0, 0, 1, 1)
}), (
    'foo/*z', 'foo/bba/arr', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    'foo/**z', 'foo/bba/arr', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (0, 0, 0, 0, 0, 0)
}), (
    'foo?bar', 'foo/bar', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 0, 0),
        'pywildmatch': (1, 1, 0, 0, 0, 0)
}), (
    'foo[/]bar', 'foo/bar', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 0, 0),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'foo[^a-z]bar', 'foo/bar', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 0, 0),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '*Xg*i', 'ab/cXd/efXg/hi', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 0, 0),
        'pywildmatch': (1, 1, 0, 0, 0, 0)
}), (
    '[A-Z]', 'a', {
        'python_fnmatch': (0, 1),
        'libgit2': (0, 1, 0, 1),
        'pywildmatch': (0, 1, 0, 1, 0, 1)
}), (
    '[A-Z]', 'A', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[a-z]', 'A', {
        'python_fnmatch': (0, 1),
        'libgit2': (0, 1, 0, 1),
        'pywildmatch': (0, 1, 0, 1, 0, 1)
}), (
    '[a-z]', 'a', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[[:upper:]]', 'a', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 1, 0, 1),
        'pywildmatch': (0, 1, 0, 1, 0, 1)
}), (
    '[[:upper:]]', 'A', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[[:lower:]]', 'A', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 1, 0, 1),
        'pywildmatch': (0, 1, 0, 1, 0, 1)
}), (
    '[[:lower:]]', 'a', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[B-Za]', 'A', {
        'python_fnmatch': (0, 1),
        'libgit2': (0, 1, 0, 1),
        'pywildmatch': (0, 1, 0, 1, 0, 1)
}), (
    '[B-Za]', 'a', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[B-a]', 'A', {
        'python_fnmatch': (0, 1),
        'libgit2': (0, 1, 0, 1),
        'pywildmatch': (0, 1, 0, 1, 0, 1)
}), (
    '[B-a]', 'a', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    '[Z-y]', 'z', {
        'python_fnmatch': (0, 1),
        'libgit2': (0, 1, 0, 1),
        'pywildmatch': (0, 1, 0, 1, 0, 1)
}), (
    '[Z-y]', 'Z', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}))


if __name__ == '__main__':
    from __init__ import validate_data
    for dataset in DATA:
        validate_data(dataset),
    print(__file__, len(DATA), 'tests'),
