
pywildmatch TESTING
-------------------

#### INDIVIDUAL TESTS

pywildmatch has a lot tests, and a few ways of using those tests.<br>

pywildmatch tests are most accessible when run via python module.<br>

Basic pywildmatch.test module syntax can be discovered like this...
```
    $ python3 -m pywildmatch.test --help
```

<br>

As a reminder, individual patterns can be tested against a string using the pywildmatch module.<br>

The pywildmatch module syntax can be seen like so...
```
    $ python3 -m pywildmatch --help
```

<br>
 
Example pywildmatch module usage goes like this...
```
    $ python3 -m pywildmatch --pattern='foo?ar' --text='foobar'
```

<br>
 
Because pywildmatch has overlap with python-fnmatch and libgit2-wildmatch (and uses their tests, too),
it can be helpful to see how these all compare.<br>

pywildmatch tests are organized like a matrix.<br>

There are 3 "matchers", functions which implement matching for each of pywildmatch, python-fnmatch, and libgit2-wildmatch.<br>

There are 3 test suites.  The suites have test data, as well as expected test results.<br>

Each of the test suites ‒ again, pywildmatch, python-fnmatch, and libgit2-wildmatch ‒ has results for all 3.<br>

Not all of the tests will pass for each usage, but you can use the `--show` option to examine how they differ.<br>

Here's an example using pywildmatch against the libgit2 tests, compared with the expected results for libgit2...
```
    $ python3 -m pywildmatch.test --matcher pywildmatch --suite libgit2 --result libgit2 --show
```

#### TEST OUTPUT

When using the `--show` option, test output will be formatted as follows...
```
    RESULT: <result>
    PATTER: <pattern>
    REGX:   <regular expression>
    METHOD: <method>
    TEXT:   <text>
    SPAN:   <indices>
    GROUP:  <group>
    OPTS:   <options>
```

<br>

`RESULT` is one of:<br>
• **`∈`** character indicating element of set.  It is a match.<br>
• **`∅`** character indicating an empty set.  It is not a match.<br>
• **`∉`** character means result has no membership in set.  This is a negated match.<br>

<br>

**`PATTER`** is the wildmatch pattern used for the test.<br>

<br>

**`REGX`** is the regular expression generated from the wildmatch pattern.<br>

<br>

**`METHOD`** is the regular expression method used, "search" or "match".<br>

<br>

**`TEXT`** is the text against which the wilmatch pattern is tested.<br>

<br>

**`SPAN`** shows the beginning and ending indices of the match, if any.<br>

<br>

**`GROUP`** is the string matched by the pattern, if any.<br>

<br>

**`OPTS`** lists the options used for the match.  It is a explaination of the flag used.<br>

<br>


#### UNIT TESTS

Tests for pywildmatch unit testing are found here:<br>
• `tests/test_match_one.py`<br>
• `tests/test_error.py`<br>

<br>

pywildmatch exceptions are tested with `test_error.py`.<br>

Usage for this script can be found as expected...
```
    $ python3 tests/test_error.py --help
```

<br>

The `test_match_one.py` script is a reimplementation of tests from `src/pywildmatch/test`.<br>
Its just that they're the tests specifically for pywildmatch.<br>

<br>

These unit tests are supposed to get used by pytest.<br>

<br>

---

NOTES
-----

The libgit2 matcher is implemented as system call to a file called `wildmatch.exe`.<br>
That file is not included in this project.<br>
It would have to be built from libgit2 source and `src/pywildmatch/test/extra/wildmatch_exe.c`<br>

<br>

The pywildmatch matcher tests are really `Match.match_one` tests.<br>
Tests still needed for `match_any` and `Match.match_many`.<br>


