
* You can include multiple blocks in a single `awk` command. The blocks are executed in the sequence they appear, and they are separated by semicolons.
```bash
$ awk 'BEGINFILE { print "Processing file: " FILENAME; } { print $0; }' file1.txt file2.txt
```

**Output**
```
Processing file: employee.txt
ajay manager account 45000
sunil clerk account 25000
varun manager sales 50000
amit manager account 47000
tarun peon sales 15000
deepak clerk sales 23000
sunil peon sales 13000
satvik director purchase 80000

Processing file: employee1.txt
ajay account
sunil account
varun sales
amit account
tarun sales
deepak sales
sunil sales
satvik purchase
```

#bash 