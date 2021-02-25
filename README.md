pywildmatch
-----------

pywildmatch is a python library for pattern matching based on wildmatch.<br>

Similar to python fnmatch, the pattern is converted to a regular expression.<br>

Unlike fnmatch, wildmatch is far more expressive than a shell-style glob.<br>

Wildmatch patterns are also easier to read than regular expressions.<br>

Wildmatch is used by git, too.  You're already using it in your gitignore files.<br>

pywildmatch is comprised of the python3 stardard library only, no additional dependencies.<br>

A simple example of pywildmatch looks like this...<br>

```python
    from pywildmatch import Match
    from pywildmatch.disp import disp
    matcher = Match().match_one('foo?ar')
    result = matcher('foobar')
    print(result.has_match)
    disp(result)
```

To get familiar with how the matching works, try the included command line tool.<br>

```
    $ python3 -m pywildmatch --pattern='foo?ar' --text='foobar'
```


#### USEFULNESS
• configuration files<br>
• gitignore-like functionality<br>
• url routing<br>

#### WILDMATCH SYNTAX
SEE: `doc/wildmatch_syntax.md`<br>

<br>

---

OVERVIEW
--------

#### MATCH FLAGS

Where applicable, the match flag mimics the flag used by libgit2.<br>
The match flag may be passed at **`match.Match`** instantiation, or to the **`match.Match.match_one`** function.<br>
The default flag is **`WM_Match`**.<br>

**`FN_Match`**<br>

```
    from pywildmatch import FN_Match
```

Like "FNM_PATHNAME" from libgit2.<br>
This option has the highest match affinity and least specificity.<br>
The "**`*`**" pattern is equivalent to the "**`**`**" pattern, and both will match "**`/`**".<br>
Character sets can also match "**`/`**".<br>

**`WM_Match`**<br>

```
    from pywildmatch import WM_Match
```

Like "WM_PATHNAME" from libgit2.<br>
This is the matching style used by gitignore.<br>
The "**`/`**" character is conditionally matched.<br>

**`ALL_Match`**<br>

```
    from pywildmatch import ALL_Match
```

This option has the least match affinity and highest specificity.<br>
Patterns will match "**`/`**".<br>
Flag not used by libgit2.<br>

<br>

#### LIBRARY HIGHLIGHTS

MODULE: **`match`**<br>

CLASS: **`match.Match`**<br>

```
    Match(flag:int=<FLAG>, icase:bool=False, verbose:bool=False)
```

METHOD: **`match.Match.match_one`**<br>

```
    match_one(pattern:str, flag:int=None) -> FunctionType "matcher"
```

Function "matcher" takes an argument for a single string, "text".<br>
A single pattern is matched against it.<br>

```
    matcher(text:str) -> Param Type
```

METHOD: **`match.Match.match_any`**<br>

```
    match_any(patterns:List[str]) -> FunctionType "matcher"
```

Function "matcher" takes an argument for a single string, "text".<br>
Any from a list patterns is matched against "text" argument.<br>

```
    matcher(text:str) -> Param Type
```

METHOD: **`match.Match.match_many`**<br>

```
    match_many(patterns:List[str]) -> FunctionType "matcher"
```

Function "matcher" takes an argument for a single string, "text".<br>
Each from a list of patterns is matched against "text" argument.<br>

```
    matcher(text:str) -> Generator[Param Type]
```

MODULE: **`param`**<br>

CLASS: **`param.Param`**<br>

Encapsulates attributes for "matcher" function.<br>
• `pattern`<br>
• `regx`<br>
• `method`<br>
• `text`<br>
• `span`<br>
• `group`<br>
• `error`<br>
• `flag`<br>
• `negate`<br>
• `result`<br>

PROPERTY: **`param.Param.has_match`**<br>

`True` if **`Param.result`** indicates match. Otherwise `False`.<br>

MODULE: **`disp`**<br>

Utilities to show **`param.Param`** details.<br>

FUNCTION: **`disp.disp`**<br>

```
    disp(param: Param Type)
```

Display meaningful details of **`param.Param`** object.<br>
The standard python logger is used, outputting to stdout if no logger is found or specified.<br>

Symbols displayed for "RESULT".<br>
• **`∈`** Result belongs to match.<br>
• **`∅`** No match. Empty set.<br>
• **`∉`** Result does not belong to match. Its negated.<br>

<br>

---

CMDLINE TOOL
------------

This is probably the clearest way to see how matching works.<br>

Admittedly, the wildmatch syntax can take a little getting used to.<br>

To understand how the flags work, and verify whether a pattern does what you expect, you can test it first.<br>

Test patterns can come from a gitignore file, or be given individually.<br>

ARGUMENTS:<br>
• `--help`<br>
• `--pattern`<br>
• `--file`<br>
• `--text`<br>
• `--match`<br>
• `--ignorecase`<br>

REQUIRED ARGUMENTS:<br>
• `--pattern` or `--file`<br>
• `--text`<br>

ARGUMENT DEFAULTS:<br>

`--match=WM_Match` is the default match flag.<br>

USAGE:<br>

```
    $ python3 -m pywildmatch --help
```

EXAMPLE:<br>

```
    $ python3 -m pywildmatch --pattern='foo?ar' --text='foobar'
    RESULT:  ∈
    PATTER:  foo?ar
    REGX:  foo[^/]ar$
    METHOD:  match
    TEXT:  foobar
    SPAN:  (0, 6)
    GROUP:  foobar
    OPTS:  wildmatch
```

NOTE:<br>
• Use quotations, even single-quotes, for patterns with tricky characters.<br>
• Long-style arguments, including an "**`=`**", may be helpful.<br>

<br>

---

SUGGESTED INSTALL
-----------------

```
    $ cd pywildmatch
    $ sudo python3 setup.py --verbose install
```

TESTS
-----

SEE: `src/pywildmatch/test/README.md`<br>

