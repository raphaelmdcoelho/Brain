Two-way I/O in `awk` allows you to both read from and write to a command or a file within the same script. This is particularly powerful when you need to interact with external processes or when you want to update a file based on some conditions.

### Concept

Two-way I/O is often used with the `|&` operator in `awk`. This operator opens a two-way pipe to a command, enabling both reading and writing operations. You can also use it with filenames for similar read/write access.

### Examples

**Two-way I/O with Command**
```bash
BEGIN {
  "bc" |&  # start the bc process
  print "2+3" |& "bc"  # write to bc
  "bc" |& getline result  # read from bc
  print "Result: " result  # display the result
  close("bc")  # close the bc process
}
```

**Two-way I/O with File**
```bash
BEGIN {
  file = "example.txt"
  print "Line 1" > file
  print "Line 2" > file
  close(file)  # Close for writing

  while ((getline line < file) > 0) {
    print "Read: " line  # Read from file
  }
  close(file)  # Close for reading
}
```

Back [[Technology/BASH/AWK/AWK]]

#bash #awk