- The operator ">" redirects the output to a new file or overwritten the content of it.
- the operator ">>" redirects the output to a new file or append the content to it.
- file descriptors:
	- stdin: 0
	- stdout: 1
	- stderr: 2
- eg:
		```command > file.txt
		command 1> file.txt```
		
- Redirects a stderr and stdout to a file:
	 ```command &> file.txt``` (modern way).
	 ```command >file 2>&1```
- Combining stdin and stdout:
	 ```sort < unsorted.txt > sorted.txt```

#bash 