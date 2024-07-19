pywildmatch
-----------

pywildmatch is a python library for text pattern matching based on wildmatch.<br>

pywildmatch implements features for gitignore and file path matching.<br>

<br>

#### EXAMPLE USAGE

```python
    from pywildmatch import Match
    match = Match("foo?ar")
    match("foobar")
```

```python
    from pywildmatch import Ignore
    ignore = Ignore(".gitignore")
    ignore("some/filepath")
```

To get familiar with how the matching works, try the included command line tool.<br>

```
    $ python3 -m pywildmatch --pattern='foo?ar' --text='foobar'
```

```
    $ python3 -m pywildmatch --file=.gitignore --text='some/filepath'
```

<br>

---

INSTALL
-------

```
    $ cd pywildmatch
    $ python3 -m pip install .
```

pywildmatch is comprised of the python3 stardard library only, no additional dependencies.<br>

<br>

---

OVERVIEW
--------

Similar to python fnmatch, pywildmatch generates a regular expression from a given pattern.<br>

Unlike fnmatch, wildmatch is far more expressive than a shell-style glob.<br>

Wildmatch patterns are also easier to read than regular expressions.<br>

Wildmatch is used by rsync and git.  You're already using it in your gitignore files.<br>

#### LIBRARY FEATURES AND USE
SEE: `doc/pywildmatch_documentation.md`<br>

#### WILDMATCH SYNTAX
SEE: `doc/wildmatch_syntax.md`<br>

<br>

---

TESTS
-----

pywildmatch uses pytest. With pytest installed, it may be invoked as follows...<br>

```
    $ cd pywildmatch
    $ pytest
```

There are about 4470 individual unit tests, plus an additional 2204 unit tests<br>
for validation with python fnmatch and libgit2.<br>

pywildmatch is also mypy compliant.<br>

<br>
