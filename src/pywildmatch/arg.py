
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

from argparse import ArgumentParser, SUPPRESS

from pywildmatch._lib import *


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# CMDLINE ARGS

match_fnmatch = sre_compile(r'fn\w*?', IGNORECASE).match
match_wildmatch = sre_compile(r'wm\w*?|wild.\w*?', IGNORECASE).match
match_all = sre_compile(r'all\w*?', IGNORECASE).match


# MATCH FLAG FROM ARGS OBJ
def get_match_flag(args):
    flag = args.flag
    if flag is None:
        flag = WM_Match
    elif flag.isnumeric():
        flag = int(flag)
    elif match_fnmatch(flag):
        flag = FN_Match
    elif match_wildmatch(flag):
        flag = WM_Match
    elif match_all(flag):
        flag = ALL_Match
    else:
        return
    if not (flag&1) and args.icase:
        flag += 1
    return flag


def get_args(help=str()):
    join = lambda *args: '\n'.join(*args)
    if help:
        parser = ArgumentParser(
            add_help = False,
            usage = SUPPRESS,
        )
        parser.add_argument(
            '-h', '--help',
            action = 'store_true',
            dest = 'help'
        )
        def exit(msg):
           parser.exit(1, join((msg,help)))
    else:
        parser = ArgumentParser(
            usage = SUPPRESS
        )
        def exit(msg):
           print(msg, end='\n\n')
           parser.print_help()
           parser.exit(1)

    parser.add_argument(
        '-f', '--file',
        action = 'store',
        dest = 'ignorefile',
        metavar = '<IGNOREFILE>'
    )
    parser.add_argument(
        '-p', '--pattern',
        action = 'store',
        dest = 'pattern',
        metavar = '<PATTERN>'
    )
    parser.add_argument(
        '-t', '--text',
        action = 'store',
        dest = 'text',
        help = 'REQUIRED',
        metavar = '<TEXT>',
    )
    # OPTIONAL
    parser.add_argument(
        '-m', '--match',
        action = 'store',
        dest = 'flag',
        help = 'OPTIONAL',
        metavar = '<MATCH FLAG>'
    )
    parser.add_argument(
        '-i', '--ignorecase',
        action = 'store_true',
        dest = 'icase',
        help = 'OPTIONAL'
    )
    # NOTE: verbose MAY NOT BE IMPLEMENTED
    parser.add_argument(
        '-v', '--verbose',
        action = 'store_true',
        dest = 'verbose',
        help = 'OPTIONAL'
    )
    # ARGUMENT OBJECT
    args = parser.parse_args()
    # MATCH FLAG
    args.flag = get_match_flag(args)
    if args.flag is None:
       exit(join((
           'ERROR. --match FLAG, IF GIVEN, MUST BE ONE OF:',
           '  `fn`',
           '  `wm`',
           '  `all`',
           'DEFAULT IS `wm`'
       )))
    # HELP SUPPLIED BY CALLER
    if getattr(args, 'help', None):
        parser.exit(0, help)
    # HELP
    if any((
        not args.text,
        args.pattern and args.ignorefile,
        not args.pattern and not args.ignorefile
    )):
       exit(
           'ERROR. ARGUMENT REQUIRED FOR '
           'EITHER IGNOREFILE OR PATTERN.'
       )
    return args


