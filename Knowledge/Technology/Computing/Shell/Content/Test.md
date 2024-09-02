
## Concept

It's a way to check/test the result for a given expression condition

## Syntax

```
[1 -lt 2]

[[ $NAME -eq "Value" ]]
```

### Examples

```bash
[ expression ]
    $ [ -d ./file.txt ]
    $ [ -f ./file.txt ]
    $ [ -e ./file.txt ]
    $ [ -s ./file.txt ]
    $ [ -w ./file.txt ]
    $ [ -r ./file.txt ]
    $ [ -x ./file.txt ]
    $ [ -z "string" ]
    $ [ -n "string" ]
    $ [ "string1" = | != "string2" ]
    $ [ "$VARIABLE" = "string" ]
    $ [ arg1 eq arg2 ]
    $ [ arg1 ne arg2 ]
    $ [ arg1 lt arg2 ]
    $ [ arg1 le arg2 ]
    $ [ arg1 gt arg2 ]
    $ [ arg1 gearg2 ]
```

#technology #computing #shell 