'''
TEST WHETHER A WILDMATCH PATTERN MATCHES A STRING
GIVE ARG FOR --pattern OR --file
MUST GIVE ARG FOR --text

USAGE:
  -p, --pattern)
      THIS IS THE WILDMATCH PATTERN

  -f, --file)
      PATH TO GITIGNORE FILE
      TEST THESE PATTERNS AGAINST STRING

  -t, --text)
      MATCH THIS STRING AGAINST A WILDMATCH PATTERN
      *REQUIRED

  -m, --match)
      fn, FN)
        APPROXIMATES FNMATCH
      wm, WM)
        PATTERN MATCHES LIKE GIT WILDMATCH
        DEFAULT
      all, ALL)
        PATTERN MATCHES ALL CHARACTERS, INCLUDING "/"
      *MATCH FLAG IS OPTIONAL

  -i, --ignorecase)
      DEFAULT IS CASE SENSITIVE
      *OPTIONAL

  -h, --help)
      OH CAROLINE NO
'''


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

from pywildmatch import Match
from pywildmatch.arg import get_args
from pywildmatch.disp import disp
from pywildmatch.config import read_gitignore


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# COMMAND TESTS

def pywildmatch_cmd(pattern, text, flag):
    wm = Match(flag, verbose=True)
    matcher = wm.match_one(pattern)
    param = matcher(text)
    disp(param)


def pywildmatch_many_cmd(patterns, text, flag):
    wm = Match(flag, verbose=True)
    matcher = wm.match_many(patterns)
    for param in matcher(text):
        disp(param)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# MAIN

args = get_args(globals()['__doc__'])

if args.ignorefile:
    patterns = read_gitignore(args.ignorefile)
    pywildmatch_many_cmd(
        patterns,
        args.text,
        args.flag
    )
elif args.pattern:
    pywildmatch_cmd(
        args.pattern,
        args.text,
        args.flag
    )


