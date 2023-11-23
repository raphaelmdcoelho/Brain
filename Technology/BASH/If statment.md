```bash
if [ ! -e ./*.sql ]; then echo "message"; fi`
```

```bash
if [ 1 -eq 2 ]; then echo "is equal"; else echo "not equal"; fi;
```

```bash
if [[ 1 -eq 2 ]]
	echo ""
elif [[ 1 -eq 2 ]]
	echo ""
else
	echo ""
```

### Bash file conditions 

* -e => Checks if the file exists or not.
* -d => Checks if the file is a directory.
* -b => Checks if the file is a block device.
* -c => Checks if the file is a character device.
* f1 -nt f2 => If file f1 is newer than file f2.
* f1 -ot f2 => If file f1 is older than file f2.
* -r => File can be read (read permission).
* -w => File can be modified (write permission).
* -x => File can be executed (execute permission).

<hr>
### Bash Number Conditions

* num1 **-eq** num2 => Check if numbers are equal.
* num1 **-ne** num2 => Check if numbers are not equal.
* num1 **-lt** num2 => Checking if num1 is lower than num2.
* num1 **-le** num2 => Lower or equal than num2.
* num1 **-gt** num2 => Greater than num2.
* num1 **-ge** num2 => Greater or equal than num2.

<hr>
## Bash String Conditions

* str1 **=** str2|l => Checks if strings are equal or not.
* str1 **!=** str2 => Checks if strings are different.
* -z str1 => Checks if str1 is empty.
* -n str1 => Checks if str1 is not empty.

#bash 