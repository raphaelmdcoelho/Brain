
## Syntax

### How to declare a bash variable

```bash
NAME="Value"
```

### How to read a variable value

```bash
echo $NAME

echo ${NAME}
```

### Sign a value from another variable

```bash
NAME=$(whoami)
```

### How to set create a environment variable (Linux)

```bash
export VARIABLE_NAME="Value"
```


## Local variable

A local variable value will be available only inside of the function scope

```bash
function run {
	local NAME=($1)
	echo $NAME
}
```
## Summary

```bash
export NAME=$(ANOTHER_VARIABLE)
echo "This is the value ${NAME}"
```

#technology #computing #shell