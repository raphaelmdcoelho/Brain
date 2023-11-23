operates by reading input, line by line, applying operations specified in its command-line arguments, and then outputting the modified lines. The basic syntax of `sed` is:

```bash
sed [options] 'command' file
```

**Basic Text Substitution**: The most common use of `sed` is to replace text. The syntax for this is `s/pattern/replacement/`. For example:

```bash
sed 's/apple/orange/' file.txt
```

#bash