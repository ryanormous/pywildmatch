
BACKGROUND
----------

There are several earlier implementations of wildmatch, inspired<br>
by Rich Salz wildmat, including flavors used in rsync and git.<br>
Although little details vary between these versions, pywildmatch<br>
most closely follows libgit2 wildmatch.<br>

<br>

---

PATTERN SYNTAX
--------------

Remember, pattern matching may differ depending on the match flagi<br>
used.<br>

#### SPECIAL CHARACTERS

• "**`?`**"<br>
Matches any single character, but not slash "`/`".<br>

• "**`*`**"<br>
Matches multiple characters, but not slash "`/`".<br>

• "**`**`**"<br>
Matches multiple characters, including slash "`/`".<br>

Additional "`*`" characters are benignly consumed after "`**`".<br>
So "`***`" or "`****`" becomes "`**`".<br>


#### CHARACTER SET

• "**`[`**" and "**`]`**"<br>
Match the stuff between the square brackets.<br>
Set matching can be negated beginning with "**`[^`**" or "**`[!`**".<br>

Except for "**`[!`**" negation, the pywildmatch "CHARACTER SET" is<br>
directly implemented by the python regular expression character set.<br>
Basically you can use it the same way as python allows.<br>

An empty "CHARACTER SET" is an error in pywildmatch.<br>
A nested "CHARACTER SET" is a pywildmatch error, too.<br>


#### CHARACTER CLASS

• **`[:alnum:]`**<br>
`re.compile("[0-9A-Za-z]")`

• **`[:alpha:]`**<br>
`re.compile(r"[\w]")`

• **`[:blank:]`**<br>
`re.compile(r"[\s]")`

• **`[:cntrl:]`**<br>
`re.compile(r"[\x00-\x1f\x7f-\xa0]")`

• **`[:digit:]`**<br>
`re.compile(r"[\d]")`

• **`[:graph:]`**<br>
`re.compile(r"[\S]")`

• **`[:lower:]`**<br>
`re.compile("[a-z]")`

• **`[:print:]`**<br>
`re.compile(r"[\S]")`

• **`[:punct:]`**<br>
`re.compile(r"[\W]")`

• **`[:space:]`**<br>
`re.compile(r"[\s]")`

• **`[:upper:]`**<br>
`re.compile("[A-Z]")`

• **`[:xdigit:]`**<br>
`re.compile("[0-9A-Fa-f]")`

NOTE:<br>
**`[:blank:]`** same as **`[:space:]`**<br>
**`[:graph:]`** same as **`[:print:]`**<br>

Some "CHARACTER CLASS" patterns can be used outside of a<br>
"CHARACTER SET", and some cannot.<br>
The distinction is whether a "CHARACTER CLASS" expresses a<br>
range of characters.<br>

This is a range: `re.compile("[0-9A-Za-z]")`<br>
This is not a range: `re.compile(r"[\d]")`<br>

A "CHARACTER CLASS" expressing a range must go inside a<br>
"CHARACTER SET".<br>


#### NEGATION

• "**`!`**"<br>
When used at the beginning of a pattern, the entire match is<br>
negated.<br>
Significant also when used at the beginning of a "CHARACTER SET".<br>

• "**`^`**"<br>
Significant only when used at the beginning of a "CHARACTER SET".<br>


#### FORBIDDEN CHARACTERS

• "**`$`**"<br>
• "**`(`**" and "**`)`**"<br>
• "**`{`**" and "**`}`**"<br>
• "**`'`**" SINGLE QUOTE<br>
• "**`"`**" DOUBLE QUOTE<br>

If used, these must be escaped.

<br>

---

DIFFERENCES BETWEEN pywildmatch AND libgit2 WILDMATCH
-----------------------------------------------------

#### "CHARACTER SET" WILL MATCH "**`/`**"

For pywildmatch these are matches using any flag.<br>

PATTERN: `foo[/]bar`<br>
TEXT: `foo/bar`<br>

PATTERN: `foo[^a-z]bar`<br>
TEXT: `foo/bar`<br>


#### BEHAVIOR OF "**`**`**" FOLLOWED BY "**`/`**"

This is a match using the **`WM_MATCH`** flag, but not with<br>
the **`PW_MATCH`** flag.<br>

PATTERN: `foo/**/**/bar`<br>
TEXT: `foo/bar`<br>

This also matches using the **`WM_MATCH`** flag, but not<br>
**`PW_MATCH`** because the "**`/`**" must be matched.<br>

PATTERN: `foo**/bar`<br>
TEXT: `foobar`<br>

<br>

---

ADDITIONAL INFO
---------------

#### TIPS

Repetition of patterns in config file, gitignore file, should<br>
be avoided.<br>

A trailing slash for a pattern is intended to match a directory,<br>
just like rsync.<br>

