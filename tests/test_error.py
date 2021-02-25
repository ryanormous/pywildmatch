
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

from argparse import ArgumentParser
from unittest import (
    TestCase as CaseTest,
    TestSuite as SuiteTest,
    TextTestRunner
)
from pywildmatch import Match
from pywildmatch.error import *


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# ARGS

def get_args():
    parser = ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '--show',
        action = 'store_const',
        const = 'show',
        dest = 'action'
    )
    group.add_argument(
        '--test',
        action = 'store_const',
        const = 'test',
        dest = 'action',
    )
    args = parser.parse_args()
    if args.action is None:
        return 'test'
    return args.action


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# ERRORS

# WildmatchError(Exception)
# CharError(WildmatchError)
# InputError(WildmatchError)
# MatchFlagError(WildmatchError)
# LexiconError(CharError)

DATA = ((
    # BadCharacterSetError(CharacterSetError)
    'foo[bar', BadCharacterSetError
), (
    # EmptyCharacterSetError(CharacterSetError)
    'foo[]bar', EmptyCharacterSetError
), (
    # NestedCharacterSetError(CharacterSetError)
    'foob[a-b[r]]', NestedCharacterSetError
), (
    # CharacterEscapeError(WildmatchError)
    'fooba\\z', CharacterEscapeError
), (
    # CharacterEscapeError(WildmatchError)
    # sre_constants.error: octal escape value \400 outside of range 0-0o377
    'fooba\\400z', CharacterEscapeError
), (
    # CharacterEscapeError(WildmatchError)
    # sre_constants.error: bad escape
    'foo\\U00110000z', CharacterEscapeError
    # ALSO: '\U00110000'
    # SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes ...
), (
    # CharacterClassNameError(CharError)
    'foo[:error:]', CharacterClassNameError
), (
    # CharacterClassSyntaxError(CharError)
    'foo[:xdigit:]', CharacterClassSyntaxError
), (
    # SpecialCharacterError(CharError)
    'foo|bar', SpecialCharacterError
))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# TEST

def test():
    class ErrorTest(CaseTest):
        def __init__(self, pattern, exc):
            super().__init__()
            self.pattern = pattern
            self.exc = exc
        def runTest(self):
            with self.assertRaises(self.exc):
                Match().match_one(self.pattern)
    suite_test = SuiteTest()
    for data in DATA:
        suite_test.addTest(ErrorTest(*data))
    TextTestRunner(verbosity=0).run(suite_test)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# SHOW

def show():
    for pat,exc in DATA:
        try:
            Match().match_one(pat)
        except exc as e:
            print(e.__class__.__name__, e, '\n')


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# MAIN

action = get_args()
if action == 'show':
    show()
else:
    test()

