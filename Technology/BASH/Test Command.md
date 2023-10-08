The symbol `[]` is used to evaluate contidions, but shell has a newest version of it `[[]]`.

```bash
var="value with spaces"
if [ "$var" = "value with spaces" ]; then
    echo "True"
fi
```

```bash
var="value with spaces"
if [[ $var = "value with spaces" ]]; then
    echo "True"
fi
```

#bash