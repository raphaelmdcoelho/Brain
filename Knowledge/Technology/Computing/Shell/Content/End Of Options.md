
## Concept

The `--` (double-dash) in a shell command indicates the end of options and incapacitates further option processing for the Unix or Linux command

## Why use it

With the End Of Options command is possible to say to a binary that you don't want to pass any other options to the command, so run the command in safer way avoiding not require options to be interpreted like:

**Find the value name in the text file**

```bash
ls | grep name file.txt
```

**Find the value -v in the text file**
**Note: Usually -v option is to display all matching values instead of the one used in grep filter**

```bash
ls | grep -- -v file.txt
```

## Summary

```bash
echo -- -e
```

#technology #computing #shell 