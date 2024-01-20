- The operator `>` redirects the output to a new file or overwritten the content of it.
- the operator `>>` redirects the output to a new file or append the content to it.
- file descriptors:
	- stdin: 0
	- stdout: 1
	- stderr: 2
- eg:
```bash
command > file.txt
ls exists 1> file.txt # redirect the standard output to a file
ls exists 2> file.txt # redirect the standard error output to a file
ls 2>&1 > out.txt # redirect standard output and error to a file
ls > /dev/null # discard standard output and error
read foo # read from standard input and write to a variable
```
		
- Redirects a stderr and stdout to a file:
	 ```command &> file.txt``` (modern way).
	 ```command >file 2>&1```
- Combining stdin and stdout:
	 ```sort < unsorted.txt > sorted.txt```

#bash 