# DATA = (
#     '<PATTERN>', '<TEXT>', {<RESULTS>}
# )

DATA = ((
# ANYTHING
    '?**/**0', '_Ab/210', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A**/**?', 'ABc/10_', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A**/?**0', 'ABc/_10', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A**?**0', 'ABc_210', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A**?*0', 'ABc_210', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A*?**0', 'Ab_/210', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 0, 0),
        'pywildmatch': (1, 1, 0, 0, 1, 1)
}), (
# CHARACTER CLASS
    'A**[:digit:]**0', 'A10', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A**[:digit:]*0', 'A10', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A*[:digit:]**0', 'A10', {
        'python_fnmatch': (0, 0),
        'libgit2': (0, 0, 0, 0),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
# CHARACTER SET
    'A**/[a-f]**0', 'A/b0', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A**/[a-f]*0', 'A/b0', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A**[a-f]**0', 'Ab0', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A**[a-f]*0', 'Ab0', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A**[a-f]/**0', 'Ab/0', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A**[a-f]/*0', 'Ab/0', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A*/[a-f]**0', 'A/b0', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A*[a-f]**0', 'Ab0', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A*[a-f]/**0', 'Ab/0', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A[a-f]**/**0', 'Ab/0', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A[a-f]**/*0', 'Ab/0', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A[a-f]**0', 'Ab0', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A[a-f]*/**0', 'Ab/0', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
# ESCAPE + ESCAPE
    'A**\\\\**0', 'Ab&\\\\10', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A**\\\\*0', 'Ab&\\\\10', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A*\\\\**0', 'Ab&\\\\10', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A*\\\\\\\\**0', 'Ab&\\\\\\\\10', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
# ESCAPE + SPECIAL CHARACTER
    'A**\\+**0', 'Abሴ++ሴ10', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A**\\+*0', 'Abሴ++ሴ10', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A*\\+**0', 'Abሴ++ሴ10', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A*\\+\\+**0', 'Abሴ++ሴ10', {
        'python_fnmatch': (0, 0),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
# UNICODE CHARACTER
    'A**🛧**0', 'Ab🛧10', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A**🛧*0', 'Ab🛧10', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A*🛧**0', 'Ab🛧10', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
# OCTAL
    'A**\046**Z', 'A&Z', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A**\046*Z', 'A&Z', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A*\046**Z', 'A&Z', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A*\046\046**Z', 'A&&Z', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
# HEX
    'A**\xff**0', 'Aÿ0', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A**\xff*0', 'Aÿ0', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A*\xff**0', 'Aÿ0', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A*\xff\xff**0', 'Aÿÿ0', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
# 16 BIT UNICODE
    'A**\u0123**Z', 'AģZ', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A**\u0123*Z', 'AģZ', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A*\u0123**Z', 'AģZ', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A*\u0123\u0123**Z', 'AģģZ', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
# 32 BIT UNICODE
    'A**\U00001234**Z', 'AሴZ', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A**\U00001234*Z', 'AሴZ', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A*\U00001234**Z', 'AሴZ', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}), (
    'A*\U00001234\U00001234**Z', 'AሴሴZ', {
        'python_fnmatch': (1, 1),
        'libgit2': (1, 1, 1, 1),
        'pywildmatch': (1, 1, 1, 1, 1, 1)
}))


if __name__ == '__main__':
    from __init__ import validate_data
    for dataset in DATA:
        validate_data(dataset)
    print(__file__, len(DATA), 'tests')


