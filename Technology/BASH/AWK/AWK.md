## Concept

Awk is a scripting language used for manipulating data and generating reports.

Everything inside the quotes mark is considered the program and it is consists of a single *pattern-action statment*.

`awk` filter each row using the **pattern** provided and if the pattern matches, then the **action** is applied.

### Structure of a AWK program

`'pattern {action}'`

Actions are embreceded between curly braces because they are optional like the patterns, so we can have a awk program with only a pattern or a action.

It is possible to run a awk program omiting the file name, so every name passed after start the program will be considered until a [[End-Of-File]] (crtl + d on Unix systems)being typed.

## Syntax

```bash
$ awk options 'selection _criteria {action}' input-file > output-file
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

## Commands

**1. Default behavior of Awk:** By default Awk prints every line of data from the specified file.  
```bash
$ awk '{print}' employee.txt
```

**Output**  
```
ajay manager account 45000
sunil clerk account 25000
varun manager sales 50000
amit manager account 47000
tarun peon sales 15000
deepak clerk sales 23000
sunil peon sales 13000
satvik director purchase 80000
```

<hr>

**2. Print the lines which match the given pattern.** 
```bash
$ awk '/manager/ {print}' employee.txt 
```

**Output**  
```
ajay manager account 45000
varun manager sales 50000
amit manager account 47000
```

* ***It's possible to have more than one criteria using &&, ! and || operators:
❗️
```bash
$ awk '/sunil/ || /5000/ {print}' employee.txt
```

**Output**
```
ajay manager account 45000
sunil clerk account 25000
varun manager sales 50000
tarun peon sales 15000
sunil peon sales 13000
```

* ***It's possible to use build-in variables to use in the filter also:
```bash
$ awk '$1=="tarun && $2=="peon" {print}' employee.txt
```

**Output**
```
tarun peon sales 15000
```

<hr>

**3. Splitting a Line Into Fields :** For each record i.e. line, the awk command splits the record delimited by whitespace character by default and stores it in the $n variables. If the line has 4 words, it will be stored in $1, $2, $3 and $4 respectively. Also, $0 represents the whole line.  
```bash
$ awk '{print $1,$4}' employee.txt 
```
**Output**  
```
ajay 45000
sunil 25000
varun 50000
amit 47000
tarun 15000
deepak 23000
sunil 13000
satvik 80000
```

<hr>

* [[Built-in Variables]]

<hr>

**To add a text to the output**
```bash
awk '{ print "Output: ", $0 * $1 }' employee.txt
```

**Fancier output**
❗️
```bash
awk '{ printf(format, value1, value2, valuen) }' employee.txt

awk '{ printf("result %-8s %s %3.2f \n", $0, $1, $2)}' emmployee.txt
```

**Sorting the output**
```bash
awk '{ printf(%s, $0)}' | sort
```

**To find/check for any string in any specific column**
```bash
$ awk '{ if($3=="account") print $0; }' employee.txt
```

**Output**
```
ajay manager account 45000
sunil clerk account 25000
amit manager account 47000
```

<hr>

**Printing lines with more than 10 characters**
```bash
$ awk 'length($0) > 27' employee.txt
```

**Output**
```
satvik director purchase 80000
```

<hr>

**To print the squares of first numbers from 1 to n say 6**
```bash
$ awk 'BEGIN { for(i=1;i<=6;i++) print "square of", i, "is", i*i; }'
```

**Output**
```
square of 1 is 1
square of 2 is 4
square of 3 is 9
square of 4 is 16
square of 5 is 25
square of 6 is 36
```

**Note**: This is a stand alone operation, without a file input, so because of that there is a BEGIN keyword at beginning. The BEGIN is asking to awk to run something, before try to read a file content. 

<hr>

* [[Special Blocks]]

<hr>

* [[Execute multiple blocks or files]]

<hr>

* [[Add awk result to a new file]]

<hr>

**Apply awk on stdout others than a file**
```bash
$ ls -l | awk '$5 > 1000 {print $9}' # filter out files of a certain size
$ ps aux | awk '$1=="username" {print $0}' # to filter processes owned by a specific user
$ curl -s "https://example.com" | awk '/pattern/ {print $0}' # filter lines from web page
$ echo "This is a text" | awk '{print $1}'
```

<hr>

### Data validation

A good use of `awk` Is to find validation errors in the data.

<hr>

* [[Associative arrays]]

* [[User-Defined Functions]]

* [[Dynamic Regular Expressions]]

* [[Built-in Functions]]

* [[Two-way I O]]

* [[Field Separators]]

* [[Advanced Control Flow]]

* [[Multi-Line Records]]

* [[Internationalization and Localization]]

* [[Debugging and Profiling]]

* [[In-Place Editing]]

* [[Networking]]

#bash #awk
