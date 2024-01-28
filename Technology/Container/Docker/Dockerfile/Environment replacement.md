
Environment variables (declared with the `ENV` statement) can also be used in certain instrunctions as variables to be interpreted by the Dockerfile.

Environment variables are notated in the Dockerfile either with `$variable_name` or `${variable_name}`.

❗️The `${variable_name}` syntax also supports a few of the standard `bash` modifiers as specified below:

* `$variable:-word}` indicates that if `variable` is set then the result will be that value. if `variable` is not set then `word` will be the result.
* `${variable:+word}` indicates that if `variable` is set then `word` will be the result, otherwise the result is the empty string.

The following variable replacements are supported in a pre-release version of Dockerfile syntax, when using the `# syntax=docker/dockerfile-upstream:master` syntax directive in your Dockerfile:

- `${variable#pattern}` removes the shortest match of `pattern` from `variable`, seeking from the start of the string.
    
    ```bash
    str=foobarbaz echo ${str#f*b}     # arbaz
    ```
    
- `${variable##pattern}` removes the longest match of `pattern` from `variable`, seeking from the start of the string.
    
    ```bash
    str=foobarbaz echo ${str##f*b}    # az
    ```
    
- `${variable%pattern}` removes the shortest match of `pattern` from `variable`, seeking backwards from the end of the string.
    
    ```bash
    string=foobarbaz echo ${string%b*}    # foobar
    ```
    
- `${variable%%pattern}` removes the longest match of `pattern` from `variable`, seeking backwards from the end of the string.
    
    ```bash
    string=foobarbaz echo ${string%%b*}   # foo
    ```
    
- `${variable/pattern/replacement}` replace the first occurrence of `pattern` in `variable` with `replacement`
    
    ```bash
    string=foobarbaz echo ${string/ba/fo}  # fooforbaz
    ```
    
- `${variable//pattern/replacement}` replaces all occurrences of `pattern` in `variable` with `replacement`
    
    ```bash
    string=foobarbaz echo ${string//ba/fo}  # fooforfoz
    ```
    

In all cases, `word` can be any string, including additional environment variables.

`pattern` is a glob pattern where `?` matches any single character and `*` any number of characters (including zero). To match literal `?` and `*`, use a backslash escape: `\?` and `\*`.

You can escape whole variable names by adding a `\` before the variable: `\$foo` or `\${foo}`, for example, will translate to `$foo` and `${foo}` literals respectively.

Examples:

```dockerfile
FROM busybox
ENV FOO=/bar
WORKDIR ${FOO}   # WORKDIR /bar
ADD . $FOO       # ADD . /bar
COPY \$FOO /quux # COPY $FOO /quux
```


#docker #container #dockerfile