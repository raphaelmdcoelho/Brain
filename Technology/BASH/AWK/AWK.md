## Concept

Awk is a scripting language used for manipulating data and generating reports.

## Syntax

```bash
$ awk options 'selection _criteria {action}' input-file > output-file
```

**Note**: the awk command receives a string '...' and inside of it, we have first a search criteria and after it the print object inside curly braces. So if necessary to format how the text will be displayed, the filter should be applied inside of curly braces print object.
## Options

-f program-file : Reads the AWK program source from the file 
                  program-file, instead of from the 
                  first command line argument.
-F fs

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

* ***It's possible to have more than one criteria using && and || operators:
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

### [[Built-in Variables]]

<hr>

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

### [[Special Blocks]]

<hr>

### [[Execute multiple blocks or files]]

<hr>

### [[Add awk result to a new file]]

<hr>

**Apply awk on stdout others than a file**
```bash
$ ls -l | awk '$5 > 1000 {print $9}' # filter out files of a certain size
$ ps aux | awk '$1=="username" {print $0}' # to filter processes owned by a specific user
$ curl -s "https://example.com" | awk '/pattern/ {print $0}' # filter lines from web page
$ echo "This is a text" | awk '{print $1}'
```

<hr>

### [[Associative arrays]]

<hr>

### [[User-Defined Functions]]


<hr>

### [[Dynamic Regular Expressions]]


<hr>

1. **Built-in Functions**: `awk` has a wide range of built-in functions for string manipulation, mathematical calculations, and more.
    
4. **Two-way I/O**: Besides reading from files and stdout, `awk` can also write to files and execute shell commands.
    
5. **Field Separators**: You can use multiple field separators or even regular expressions as field separators.
    
6. **Advanced Control Flow**: While `awk`'s syntax is simple, you can construct fairly complex control flows using `if`, `else`, `while`, `for`, etc.
    
7. **Multi-Line Records**: `awk` can handle records that span multiple lines, which is handy for dealing with data formats like XML or JSON.
    
8. **Internationalization and Localization**: `awk` supports string collation, formatting, and other locale-specific operations.
    
9. **Debugging and Profiling**: Some versions of `awk`, like `gawk`, come with debugging and profiling tools to help you optimize your scripts.
    
10. **In-Place Editing**: Though not a native `awk` feature, some people use `awk` in combination with `sed` or other tools to perform in-place file editing.
    
11. **Networking**: With GNU `awk` (gawk), you can even perform basic networking tasks like opening sockets.

#bash