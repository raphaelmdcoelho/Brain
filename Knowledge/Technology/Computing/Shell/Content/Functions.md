
A function is a way to apply the `DRY` concept allowing you to leverage a block of code and reutilize it how many times are necessary

## Syntax

```bash
function name { 
	echo "Message" 
}

name { 
	echo "Message"
}	

## Calling the function

name
```

### Sending parameters

```bash
function name {
	echo "$1"
}

name Raphael

function names {
	for NAME in $@
	do
		echo "$NAME"
	done
}

names Raphael Bruce Peter
```

## Exit Statuses

* Every command has a return status
* The exit range is 0 to 255
* Zero represents success

**Printing return value**

```bash
ls /not/here
echo "$?"
```
## Summary

```bash
name {
	echo "Message"
}

name
```
#technology #computing #shell 