
## Concept

Awk is a scripting language used for manipulating data and generating reports.

Everything inside the quotes mark is considered the program and it is consists of a single *pattern-action statment*.

`awk` filter each row using the **pattern** provided and if the pattern matches, then the **action** is applied.

### Structure of a AWK program

`'pattern {action}'`

Actions are embraced between curly braces because they are optional like the patterns, so we can have a awk program with only a pattern or a action.

It is possible to run a awk program omitting the file name, so every name passed after start the program will be considered until a [[End-Of-File]] (`crtl + d` on Unix systems) being typed.

## Syntax

```bash
$ awk options 'selection_criteria {action}' input-file > output-file
```

**Note**: the awk command receives a string '...' and inside of it, we have first a search criteria and after it the print object inside curly braces. So if necessary to format how the text will be displayed, the filter should be applied inside of curly braces print object.
## Options

❗️
-f program-file : Reads the AWK program source from the file program-file, instead of from the first command line argument.

```bash
awk -f filename # optional list of input files
```

-F fs

### Data types

There are only two types of data in awk: numbers and strings of characters.

#technology #computing #shell 