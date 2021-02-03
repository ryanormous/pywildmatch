
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

from argparse import ArgumentParser
from unittest import (
    TestCase as CaseTest,
    TestSuite as SuiteTest,
    TextTestRunner
)
from pywildmatch.disp import disp


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# GLOBAL

global args, match, max_flag, DATA


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# ARGS

def get_args():
    tests = ('libgit2', 'python_fnmatch', 'pywildmatch')
    parser = ArgumentParser()
    parser.add_argument(
        '--matcher',
        action = 'store',
        dest = 'matcher',
        choices = tests,
        required = True
    )
    parser.add_argument(
        '--suite',
        action = 'store',
        dest = 'suite',
        choices = tests,
        required = True
    )
    parser.add_argument(
        '--results',
        action = 'store',
        dest = 'results',
        choices = tests,
        required = True
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '--show',
        action = 'store_const',
        const = 'show',
        dest = 'action',
        help = 'OPTIONAL. SHOW TEST RESULTS.'
    )
    group.add_argument(
        '--test',
        action = 'store_const',
        const = 'test',
        dest = 'action',
        help = 'DEFAULT. RUN UNIT TESTS.'
    )
    return parser.parse_args()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# TEST DATA

def iterdata(show=None):
    total = len(DATA)
    info = '  \033[1mmatcher:%s  suite:%s  %s/%s  flag:%s\033[0m'
    for index,dataset in enumerate(DATA):
        pattern, text, results = dataset[0], dataset[1], dataset[2][args.results]
        for flag,expect in enumerate(results):
            if flag > max_flag:
                break
            else:
                if show:
                    print(info % (
                        args.matcher, args.suite,
                        index+1, total, flag
                    ))
                yield (pattern, text, flag, expect)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# TEST

def test():
    class MatchTest(CaseTest):
        def __init__(self, pattern, text, flag, expect):
            super().__init__()
            self.p, self.s, self.f, self.e = pattern, text, flag, expect
        def runTest(self):
            param = match(self.p, self.s, self.f)
            self.assertEqual(bool(param), bool(self.e))
    suite_test = SuiteTest()
    for data in iterdata():
        suite_test.addTest(MatchTest(*data))
    TextTestRunner(verbosity=0).run(suite_test)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# SHOW

def show():
    no_m = add_m = count = 0
    for pattern, text, flag, expect in iterdata(show=True):
        count += 1
        param = match(pattern, text, flag)
        if bool(param) and not bool(expect):
            add_m += 1
            disp(param)
        elif bool(expect) and not bool(param):
            no_m += 1
            disp(param)
    msg = '  TOTAL TESTS:%s  MISSED MATCHES:%s  ADDITIONAL MATCHES:%s'
    print(msg % (count, no_m, add_m))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# MAIN

# ARGUMENTS
args = get_args()

# MATCHER FOR TEST
if args.matcher == 'libgit2':
    from pywildmatch.test.matcher.libgit2_match import match, max_flag

elif args.matcher == 'python_fnmatch':
    from pywildmatch.test.matcher.python_fnmatch_match import match, max_flag

elif args.matcher == 'pywildmatch':
    from pywildmatch.test.matcher.pywildmatch_match import match, max_flag

# DATA SUITE FOR TEST
if args.suite == 'libgit2':
    from pywildmatch.test.data.libgit2_data import DATA

elif args.suite == 'python_fnmatch':
    from pywildmatch.test.data.python_fnmatch_data import DATA

elif args.suite == 'pywildmatch':
    from pywildmatch.test.data.pywildmatch_data import DATA

# OUTPUT ACTION FOR TEST
if args.action == 'show':
    show()
else:
    test()


