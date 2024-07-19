pywildmatch documentation
-------------------------

#### MATCH FLAGS

pywildmatch can perform pattern matching in 3 different styles.<br>
Each of these is specified by an optional match flag.<br>

• `FN_MATCH`<br>
• `WM_MATCH`<br>
• `PW_MATCH`<br>

Where applicable, the match flag mimics the flag used by libgit2.<br>

The default flag is **`WM_MATCH`**.<br>

A separate argument for case insensitivity is also accepted.<br>

<br>

**`FN_MATCH`**<br>

```python
    from pywildmatch import FN_MATCH
```

Like "FNM_PATHNAME" from libgit2.<br>
This option has the highest match affinity and least specificity.<br>
The "**`*`**" pattern is equivalent to the "**`**`**" pattern, and both will match "**`/`**".<br>
Character sets can also match "**`/`**".<br>

<br>

**`WM_MATCH`**<br>

```python
    from pywildmatch import WM_MATCH
```

Like "WM_PATHNAME" from libgit2.<br>
This is the matching style used by gitignore.<br>
The "**`/`**" character is conditionally matched.<br>

<br>

**`PW_MATCH`**<br>

```python
    from pywildmatch import PW_MATCH
```

This option has the least match affinity and highest specificity.<br>
Patterns will match "**`/`**".<br>
Flag not used by libgit2.<br>

<br>

---

#### LIBRARY HIGHLIGHTS

MODULE: **`match`**<br>
CLASS: **`match.Match`**<br>

```python
    Match(pattern:str, flag:int=<FLAG>, icase:bool=False)
```

Returns an instance used as a "matcher" function.<br>
This "matcher" function takes an argument for a single string, "text".<br>
A single pattern is matched against it and a `Parameter` object is returned for the result of the match.<br>

```python
    matcher(text:str) -> Param Type
```

<br>

MODULE: **`ignore`**<br>
CLASS: **`ignore.Ignore`**<br>

```python
    Ignore(ignorefile:str, flag:int=<FLAG>, icase:bool=False)
```

The argument for `ignorefile` may be a filepath or a newline delimited string of ignore patterns.<br>
Returns an instance used as a "matcher" function.<br>
This "matcher" function takes an argument for a single string, "text".<br>
The patterns from the `ignorefile` are matched against it and a `Parameter` object is returned for<br>
the result of the match.<br>

```python
    matcher(text:str) -> Param Type
```

<br>

MODULE: **`param`**<br>
CLASS: **`param.Param`**<br>

Encapsulates attributes for "matcher" function.<br>

• **`pattern`**<br>
The wildmatch pattern<br>
• **`regexp`**<br>
Repsentation of the pattern as a regular expssion<br>
• **`method`**<br>
The regular expssion method: search or match<br>
• **`text`**<br>
The string associated with match function result<br>
• **`span`**<br>
Regular expssion match indices, if any<br>
• **`group`**<br>
Regular expssion grouping, if any<br>
• **`error`**<br>
Message from an `Exception` object, if any<br>
• **`flag`**<br>
The match flag, option passed from argument<br>
• **`icase`**<br>
Case insensitive flag, option passed from argument<br>
• **`negate`**<br>
Option derived from pattern<br>
• **`ignore`**<br>
Indicates functionality for reading gitignore file<br>
• **`result`**<br>
Consequence of match function run against text<br>

PROPERTY: **`param.Param.has_match`**<br>
METHOD: **`param.Param.__bool__`**<br>

`True` if **`Param.result`** indicates match. Otherwise `False`.<br>

<br>

MODULE: **`log`**<br>
FUNCTION: **`log.log`**<br>

```python
    log(param: Param Type)
```

A utility to display meaningful details of **`param.Param`** object.<br>
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

<br>

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

`--match=WM_MATCH` is the default match flag.<br>

USAGE:<br>

```
    $ python3 -m pywildmatch --help
```

EXAMPLE:<br>

```
    $ python3 -m pywildmatch --pattern='foo?ar' --text=foobar
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


