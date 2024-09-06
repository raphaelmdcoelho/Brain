
Pipelining in shell scripting allows you to use the output of one command as the input for another. This is achieved using the `|` symbol, which takes the `stdout` of the command on its left and passes it as the stdin to the command on its right.

e.g.:
```bash
cal | wc -l
```

**Note**: ***cal*** is a app to prints the calendar and ***wc*** count the words in a stream that it receives.

#technology #computing #shell 