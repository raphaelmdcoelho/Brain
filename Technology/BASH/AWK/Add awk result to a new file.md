**1. Using shell redirection**
```bash
$ awk '{print $1}' employee.txt > employee1.txt
```

**2. Using internal Print-to-File feature**
```bash
$ awk '{ print $1 > "output.txt"}' input.txt 
```

**Note**: The second option can provide more control, if the output need some kind of conditionals.

#bash 