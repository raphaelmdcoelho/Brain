
1. **NR**: It counts the number of lines you've read so far. It's useful if you want to know the line number.
    
2. **NF**: Counts the number of words in the current line. For example, if a line has 5 words, `NF` would be 5.
    
3. **FS**: This tells Awk what character separates each word. By default, it's a space or a tab, but you can change it.
    
4. **RS**: This is what separates each line. Usually, it's a new line character.
    
5. **OFS**: When you want to print something, this character will be used to separate the words in the output. By default, it's a space.
    
6. **ORS**: Similar to `OFS`, but for separating lines when printing. Usually, it's a new line character.

<hr>

**Use of NR built-in variables (Display Number Row)**  
```bash
$ awk '{print NR, $0}' employee.txt 
```

**Output**  
```
1 ajay manager account 45000
2 sunil clerk account 25000
3 varun manager sales 50000
4 amit manager account 47000
5 tarun peon sales 15000
6 deepak clerk sales 23000
7 sunil peon sales 13000
8 satvik director purchase 80000
```

<hr>

**Use of NF built-in variables (Display Count Fields by Row)
```bash
$ awk '{print NF, $0}' employee.txt
```

**Output**
```
4 ajay manager account 45000
4 sunil clerk account 25000
4 varun manager sales 50000
4 amit manager account 47000
4 tarun peon sales 15000
4 deepak clerk sales 23000
4 sunil peon sales 13000
4 satvik director purchase 80000
```

<hr>

**Use of NF built-int variables (Get field values by position dynamically)**
```bash
$ awk '{print $(NF-1), $NF}' employee.txt
```

**Output**
```
account 45000
account 25000
sales 50000
account 47000
sales 15000
sales 23000
sales 13000
purchase 80000

```

<hr>

**Use of NR built-in variables (Get rows by a specific range)**
```bash
$ awk 'NR==3, NR==6 {print NR, $0}' employee.txt
```

**Output**
```
3 varun manager sales 50000
4 amit manager account 47000
5 tarun peon sales 15000
6 deepak clerk sales 23000
```

<hr>

**To print any empty line if present OR a row with not the same number of fields as the others**
```bash
$ awk 'NF < 0' employee.txt
```

**Output**
```
$
```

<hr>

**To count the lines in a file**
```bash
$awk 'END {print NR}' employee.txt
```

**Output**
```
9
```
