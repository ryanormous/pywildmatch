
# BASED ON TEST CASES FOR libgit2 ignore
# libgit2/tests/libgit2/ignore/path.c
# VERSION: v1.7.0-244


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# DATA

DATA = ((
# HONOR TEMPORARY RULES
# 0
    '/NewFolder\n/NewFolder/NewFolder',
    'File.txt',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 1
    '/NewFolder\n/NewFolder/NewFolder',
    'NewFolder',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 2
    '/NewFolder\n/NewFolder/NewFolder',
    'NewFolder/NewFolder',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 3
    '/NewFolder\n/NewFolder/NewFolder',
    'NewFolder/NewFolder/File.txt',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# ALLOW ROOT
# 4
    '/',
    'File.txt',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 5
    '/',
    'NewFolder',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 6
    '/',
    'NewFolder/NewFolder',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 7
    '/',
    'NewFolder/NewFolder/File.txt',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# IGNORE SPACE
# 8
    '/\n\n/NewFolder \n/NewFolder/NewFolder',
    'File.txt',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 9
    '/\n\n/NewFolder \n/NewFolder/NewFolder',
    'NewFolder',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 10
    '/\n\n/NewFolder \n/NewFolder/NewFolder',
    'NewFolder/NewFolder',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 11
    '/\n\n/NewFolder \n/NewFolder/NewFolder',
    'NewFolder/NewFolder/File.txt',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# INTERMITTENT SPACE
# 12
    'foo bar\n',
    'foo',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 13
    'foo bar\n',
    'bar',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 14
    'foo bar\n',
    'foo bar',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# TRAILING SPACE
# 15
    'foo \nbar  \n',
    'foo',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 16
    'foo \nbar  \n',
    'foo ',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 17
    'foo \nbar  \n',
    'bar',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 18
    'foo \nbar  \n',
    'bar ',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 19
    'foo \nbar  \n',
    'bar  ',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# ESCAPED TRAILING SPACES
# 20
    'foo\\ \nbar\\ \\ \nbaz \\ \nqux\\  \n',
    'foo',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 21
    'foo\\ \nbar\\ \\ \nbaz \\ \nqux\\  \n',
    'foo ',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 22
    'foo\\ \nbar\\ \\ \nbaz \\ \nqux\\  \n',
    'bar',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 23
    'foo\\ \nbar\\ \\ \nbaz \\ \nqux\\  \n',
    'bar ',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 24
    'foo\\ \nbar\\ \\ \nbaz \\ \nqux\\  \n',
    'bar  ',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 25
    'foo\\ \nbar\\ \\ \nbaz \\ \nqux\\  \n',
    'baz  ',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 26
    'foo\\ \nbar\\ \\ \nbaz \\ \nqux\\  \n',
    'baz ',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 27
    'foo\\ \nbar\\ \\ \nbaz \\ \nqux\\  \n',
    'qux ',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 28
    'foo\\ \nbar\\ \\ \nbaz \\ \nqux\\  \n',
    'qux',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 29
    'foo\\ \nbar\\ \\ \nbaz \\ \nqux\\  \n',
    'qux  ',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# IGNORE DIR
# 30
    'dir/\n',
    'dir',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 31
    'dir/\n',
    'dir/node',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# IGNORE DIR WITH TRAILING SPACE
# 32
    'dir/ \n',
    'dir',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 33
    'dir/ \n',
    'dir/node',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# IGNORE ROOT
# 34
    '/\n\n/NewFolder\n/NewFolder/NewFolder',
    'File.txt',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 35
    '/\n\n/NewFolder\n/NewFolder/NewFolder',
    'NewFolder',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 36
    '/\n\n/NewFolder\n/NewFolder/NewFolder',
    'NewFolder/NewFolder',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 37
    '/\n\n/NewFolder\n/NewFolder/NewFolder',
    'NewFolder/NewFolder/File.txt',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# FULL PATHS
# 38
    'Folder/*/Contained',
    'Folder/Middle/Contained',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 39
    'Folder/*/Contained',
    'Folder/Middle/More/More/Contained',
    {
        'test':     (True, True, False, False, False, False),
        'validate': (False, False)
}), (
# 40
    'Folder/**/Contained',
    'Folder/Middle/Contained',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 41
    'Folder/**/Contained',
    'Folder/Middle/More/More/Contained',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 42
    'Folder/**/Contained/*/Child',
    'Folder/Middle/Contained/Happy/Child',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 43
    'Folder/**/Contained/*/Child',
    'Folder/Middle/Contained/Not/Happy/Child',
    {
        'test':     (True, True, False, False, False, False),
        'validate': (False, False)
}), (
# 44
    'Folder/**/Contained/*/Child',
    'Folder/Middle/More/More/Contained/Happy/Child',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 45
    'Folder/**/Contained/*/Child',
    'Folder/Middle/More/More/Contained/Not/Happy/Child',
    {
        'test':     (True, True, False, False, False, False),
        'validate': (False, False)
}), (
# GLOB
# 46
    'sub/**/*.html\n',
    'aaa.html',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 47
    'sub/**/*.html\n',
    'dir',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 48
    'sub/**/*.html\n',
    'dir/sub',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 49
    'sub/**/*.html\n',
    'dir/sub/sub2/aaa.html',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 50
    'sub/**/*.html\n',
    'dir/sub/aaa.html',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 51
    'sub/**/*.html\n',
    'dir/aaa.html',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 52
    'sub/**/*.html\n',
    'sub',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 53
    'sub/**/*.html\n',
    'sub/aaa.html',
    {
        'test':     (False, False, True, True, False, False),
        'validate': (True, True)
}), (
# 54
    'sub/**/*.html\n',
    'sub/sub2/aaa.html',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# LEADING GLOB
# 55
    '*/onestar\n**/twostars\n*/parent1/kid1/*\n**/parent2/kid2/*\n',
    'dir1/onestar',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 56
  # IN IGNORED DIR
    '*/onestar\n**/twostars\n*/parent1/kid1/*\n**/parent2/kid2/*\n',
    'dir1/onestar/child',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 57
    '*/onestar\n**/twostars\n*/parent1/kid1/*\n**/parent2/kid2/*\n',
    'dir1/dir2/onestar',
    {
        'test':     (True, True, False, False, False, False),
        'validate': (False, False)
}), (
# 58
    '*/onestar\n**/twostars\n*/parent1/kid1/*\n**/parent2/kid2/*\n',
    'dir1/twostars',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 59
  # IN IGNORED DIR
    '*/onestar\n**/twostars\n*/parent1/kid1/*\n**/parent2/kid2/*\n',
    'dir1/twostars/child',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 60
    '*/onestar\n**/twostars\n*/parent1/kid1/*\n**/parent2/kid2/*\n',
    'dir1/dir2/twostars',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 61
  # IN IGNORED DIR
    '*/onestar\n**/twostars\n*/parent1/kid1/*\n**/parent2/kid2/*\n',
    'dir1/dir2/twostars/child',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 62
    '*/onestar\n**/twostars\n*/parent1/kid1/*\n**/parent2/kid2/*\n',
    'dir1/dir2/dir3/twostars',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 63
    '*/onestar\n**/twostars\n*/parent1/kid1/*\n**/parent2/kid2/*\n',
    'dir1/parent1/kid1/node',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 64
    '*/onestar\n**/twostars\n*/parent1/kid1/*\n**/parent2/kid2/*\n',
    'dir1/parent1/kid1/node/inside/parent',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 65
    '*/onestar\n**/twostars\n*/parent1/kid1/*\n**/parent2/kid2/*\n',
    'dir1/dir2/parent1/kid1/node',
    {
        'test':     (True, True, False, False, False, False),
        'validate': (False, False)
}), (
# 66
    '*/onestar\n**/twostars\n*/parent1/kid1/*\n**/parent2/kid2/*\n',
    'dir1/parent1/node',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 67
    '*/onestar\n**/twostars\n*/parent1/kid1/*\n**/parent2/kid2/*\n',
    'dir1/kid1/node',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 68
    '*/onestar\n**/twostars\n*/parent1/kid1/*\n**/parent2/kid2/*\n',
    'dir1/parent2/kid2/node',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 69
    '*/onestar\n**/twostars\n*/parent1/kid1/*\n**/parent2/kid2/*\n',
    'dir1/parent2/kid2/node/inside/parent',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 70
    '*/onestar\n**/twostars\n*/parent1/kid1/*\n**/parent2/kid2/*\n',
    'dir1/dir2/parent2/kid2/node',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 71
    '*/onestar\n**/twostars\n*/parent1/kid1/*\n**/parent2/kid2/*\n',
    'dir1/dir2/dir3/parent2/kid2/node',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 72
    '*/onestar\n**/twostars\n*/parent1/kid1/*\n**/parent2/kid2/*\n',
    'dir1/parent2/node',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 73
    '*/onestar\n**/twostars\n*/parent1/kid1/*\n**/parent2/kid2/*\n',
    'dir1/kid2/node',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# GLOB WITH PATH DELIMITER
# 74
    'foo/bar/**',
    'foo/bar/baz',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 75
    'foo/bar/**',
    'foo/bar/baz/quux',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 76
    '_*/',
    'sub/_test/a/node',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 77
    '_*/',
    'test_folder/node',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 78
    '_*/',
    '_test/node',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 79
    '_*/',
    '_test/a/node',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 80
    '**/_*/',
    'sub/_test/a/node',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 81
    '**/_*/',
    'test_folder/node',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 82
    '**/_*/',
    '_test/node',
    {
        'test':     (False, False, True, True, False, False),
        'validate': (True, True)
}), (
# 83
    '**/_*/',
    '_test/a/node',
    {
        'test':     (False, False, True, True, False, False),
        'validate': (True, True)
}), (
# 84
    '**/_*/foo/bar/*ux',
    'sub/_test/foo/bar/qux/node',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 85
    '**/_*/foo/bar/*ux',
    '_test/foo/bar/qux/node',
    {
        'test':     (False, False, True, True, False, False),
        'validate': (True, True)
}), (
# 86
    '**/_*/foo/bar/*ux',
    '_test/foo/bar/crux/node',
    {
        'test':     (False, False, True, True, False, False),
        'validate': (True, True)
}), (
# 87
    '**/_*/foo/bar/*ux',
    '_test/foo/bar/code/node',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# GLOB
# 88
    '*.foo\n**.bar\n',
    '.foo',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 89
    '*.foo\n**.bar\n',
    'xyz.foo',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 90
    '*.foo\n**.bar\n',
    '.bar',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 91
    '*.foo\n**.bar\n',
    'x.bar',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 92
    '*.foo\n**.bar\n',
    'xyz.bar',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 93
    '*.foo\n**.bar\n',
    'test/.foo',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 94
    '*.foo\n**.bar\n',
    'test/x.foo',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 95
    '*.foo\n**.bar\n',
    'test/xyz.foo',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 96
    '*.foo\n**.bar\n',
    'test/.bar',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 97
    '*.foo\n**.bar\n',
    'test/x.bar',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 98
    '*.foo\n**.bar\n',
    'test/xyz.bar',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# DIRECTORY
# 99
    '/NewFolder\n/NewFolder/NewFolder',
    'File.txt',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 100
    '/NewFolder\n/NewFolder/NewFolder',
    'NewFolder',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 101
    '/NewFolder\n/NewFolder/NewFolder',
    'NewFolder/NewFolder',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 102
    '/NewFolder\n/NewFolder/NewFolder',
    'NewFolder/NewFolder/File.txt',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# SUBDIRECTORY
# 103
    'node2\n',
    'node2',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 104
    'node2\n',
    'dir/node2',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 105
    'node2\n',
    'dir/node2/actual_node',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 106
    'node2/\n',
    'dir/node2',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 107
  # IN IGNORED DIR 'dir/',
    'node2/\n',
    'dir/node2/actual_node',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# ENSURE gitignore IN SUBDIRECTORY ONLY AFFECTS ITEMS IN SUBDIRECTORY
  # dir1
  # dir1/dir2
  # dir1/dir2/dir3
# 108
    'dir1/\ndir1/subdir/',
    'dir1/node',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 109
    'dir1/\ndir1/subdir/',
    'dir1/dir2/node',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 110
    'dir1/\ndir1/subdir/',
    'dir1/dir2/dir3/node',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 111
    'dir1/\ndir1/subdir/',
    'dir1/dir2/dir3/dir1/node',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 112
    'dir1/\ndir1/subdir/',
    'dir1/dir2/dir3/dir1/subdir/foo',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 113
    'DiR1/\nDiR1/subdir/\n',
    'dir1/node',
    {
        'test':     (False, True, False, True, False, True),
        'validate': (False, True)
}), (
# 114
    'DiR1/\nDiR1/subdir/\n',
    'dir1/dir2/node',
    {
        'test':     (False, True, False, True, False, True),
        'validate': (False, True)
}), (
# 115
    'DiR1/\nDiR1/subdir/\n',
    'dir1/dir2/dir3/node',
    {
        'test':     (False, True, False, True, False, True),
        'validate': (False, True)
}), (
# 116
    'DiR1/\nDiR1/subdir/\n',
    'dir1/dir2/dir3/dir1/node',
    {
        'test':     (False, True, False, True, False, True),
        'validate': (False, True)
}), (
# 117
    'DiR1/\nDiR1/subdir/\n',
    'dir1/dir2/dir3/dir1/subdir/foo',
    {
        'test':     (False, True, False, True, False, True),
        'validate': (False, True)
}), (
# ENSURE FILES DO NOT MATCH FOLDER CASES, DO NOT IGNORE FILES FOR FOLDER
# 118
  # dir/
    'test/\n',
    'dir/test',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 119
    'test/\n',
    'dir/TeSt',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 120
  # dir/test
    'test/\n',
    'dir/test/',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 121
    'test/\n',
    'dir/TeSt/',
    {
        'test':     (False, True, False, True, False, True),
        'validate': (False, True)
}), (
# SYMLINK TO OUTSIDE
# 122
    'symlink\n',
    'symlink',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 123
    'symlink\n',
    'lala/../symlink',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# OTHER TEST
# 124
    '/*/\n!/src\n',
    'src/foo.c',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 125
    '/*/\n!/src\n',
    'src/foo/foo.c',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 126
    '/*/\n!/src\n',
    'README.md',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 127
    '/*/\n!/src\n',
    'dist/foo.o',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 128
    '/*/\n!/src\n',
    'bin/foo',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# UNIGNORE DIR SUCCEEDS
# 129
    '*.c\n!src/*.c\n',
    'src/foo.c',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 130
    '*.c\n!src/*.c\n',
    'src/foo/foo.c',
    {
        'test':     (False, False, True, True, True, True),
        'validate': (True, True)
}), (
# CASE INSENSITIVE UNIGNORES PREVIOUS RULE, CASE SENSITIVE UNIGNORE DOES NOTHING
# 131
    '/case\n!/Case/\n',
    'case/node',
    {
        'test':     (True, False, True, False, True, False),
        'validate': (True, False)
}), (
# IGNORED SUBDIRFILES WITH SUBDIR RULE
# 132
    'dir/*\n!dir/sub1/sub2/**\n',
    'dir/a.test',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 133
    'dir/*\n!dir/sub1/sub2/**\n',
    'dir/sub1/a.test',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 134
    'dir/*\n!dir/sub1/sub2/**\n',
    'dir/sub1/sub2',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# IGNORED SUBDIRFILES WITH NEGATION
# 135
    'dir/*\n!dir/a.test\n',
    'dir/a.test',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 136
    'dir/*\n!dir/a.test\n',
    'dir/b.test',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 137
    'dir/*\n!dir/a.test\n',
    'dir/sub1/c.test',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# NEGATIVE DIRECTORY RULES ONLY MATCH DIRECTORIES
# 138
    '*\n!/**/\n!*.keep\n!.gitignore\n',
    'src',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 139
    '*\n!/**/\n!*.keep\n!.gitignore\n',
    'src/A.keep',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 140
    '*\n!/**/\n!*.keep\n!.gitignore\n',
    '.gitignore',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# ESCAPED CHARACTER
# 141
    '\\c\n',
    'c',
    {
        'test':     ('CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError'),
        'validate': (True, True)
}), (
# 142
    '\\c\n',
    '\\c',
    {
        'test':     ('CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError'),
        'validate': (False, False)
}), (
# ESCAPED NEWLINE
# 143
    '\\\nnewline\n',
    '\nnewline',
    {
        'test':     ('CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError', 'CharacterEscapeError'),
        'validate': (True, True)
}), (
# ESCAPED GLOB
# 144
    '\\*\n',
    '*',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 145
    '\\*\n',
    'foo',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# ESCAPED COMMENTS
# 146
    '#foo\n\\#bar\n\\##baz\n\\#\\\\#qux\n',
    '#foo',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 147
    '#foo\n\\#bar\n\\##baz\n\\#\\\\#qux\n',
    '#bar',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 148
    '#foo\n\\#bar\n\\##baz\n\\#\\\\#qux\n',
    '\\#bar',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 149
    '#foo\n\\#bar\n\\##baz\n\\#\\\\#qux\n',
    '##baz',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 150
    '#foo\n\\#bar\n\\##baz\n\\#\\\\#qux\n',
    '\\##baz',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 151
    '#foo\n\\#bar\n\\##baz\n\\#\\\\#qux\n',
    '#\\#qux',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 152
    '#foo\n\\#bar\n\\##baz\n\\#\\\\#qux\n',
    '##qux',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 153
    '#foo\n\\#bar\n\\##baz\n\\#\\\\#qux\n',
    '\\##qux',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# ESCAPED SLASH
# 154
    '\\\\\n\\\\preceding\ninter\\\\mittent\ntrailing\\\\\n',
    'inter\\mittent',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 155
    '\\\\\n\\\\preceding\ninter\\\\mittent\ntrailing\\\\\n',
    'trailing\\',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# ESCAPED SPACE
# 156
    'foo\\\\ \nbar\\\\\\ \n',
    'foo\\',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 157
    'foo\\\\ \nbar\\\\\\ \n',
    'foo\\ ',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 158
    'foo\\\\ \nbar\\\\\\ \n',
    'foo\\\\ ',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 159
    'foo\\\\ \nbar\\\\\\ \n',
    'foo\\\\',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 160
    'foo\\\\ \nbar\\\\\\ \n',
    'bar\\ ',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 161
    'foo\\\\ \nbar\\\\\\ \n',
    'bar\\\\',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 162
    'foo\\\\ \nbar\\\\\\ \n',
    'bar\\\\ ',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 163
    'foo\\\\ \nbar\\\\\\ \n',
    'bar\\\\\\',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 164
    'foo\\\\ \nbar\\\\\\ \n',
    'bar\\\\\\ ',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# INVALID PATTERN
# 165
    '[',
    '[f',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 166
    '[',
    'f',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# NEGATIVE PREFIX RULE
# 167
    'ff*\n!f\n',
    'fff',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 168
    'ff*\n!f\n',
    'ff',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 169
    'ff*\n!f\n',
    'f',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# NEGATIVE, MORE SPECIFIC
# 170
    '*.txt\n!/dir/test.txt\n',
    'test.txt',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}), (
# 171
    '*.txt\n!/dir/test.txt\n',
    'dir/test.txt',
    {
        'test':     (False, False, False, False, False, False),
        'validate': (False, False)
}), (
# 172
    '*.txt\n!/dir/test.txt\n',
    'outer/dir/test.txt',
    {
        'test':     (True, True, True, True, True, True),
        'validate': (True, True)
}))

