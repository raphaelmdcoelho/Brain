
## Concept

The `if` statement allows the flow control over conditions that can be `true` or `false`

```bash
if [[ $1 -lt 100 ]]
then
	echo "The number is less than 100"
fi
```

**Elif**

```bash
if [[ -f file.txt ]]
then
	echo "The file exists"
elif [[ -f text.txt ]]
then
	echo "The text exists"
else
	echo "The files don't exit"
fi
```

#technology #computing #shell 