
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

## Summary

```bash
name {
	echo "Message"
}

name
```
#technology #computing #shell 