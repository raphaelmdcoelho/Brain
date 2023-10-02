
- `BEGIN`: Executes before `awk` reads the first line of input. Commonly used for initialization.
- `END`: Executes after `awk` has read all lines of input. Often used for <mark>summarization tasks</mark>.
- `BEGINFILE`: Executes before `awk` reads the first line from each input file. Useful when processing multiple files.
- `ENDFILE`: Executes after `awk` has read the last line from each input file.

<hr>

**BEGIN**
```bash
$ awk 'BEGIN { print "This is the header"; }'
```

**Output**
```
This is the header
```

<hr>

**END**
```bash
$ awk 'END { print "This is the footer"; }'
```

**Output**
```
This is the footer
```

<hr>

**BEGINFILE**
```bash
$ awk 'BEGINFILE { print "Processing file: " FILENAME; }' employee.txt
```

**Output**
```
Processing file: employee.txt
```

<hr>

**ENDFILE**
```bash
$ awk 'ENDFILE { print "Finished processing file: " FILENAME; }' employee.txt
```

**Output**
```
Finished processing file: employee.txt
```

#bash 