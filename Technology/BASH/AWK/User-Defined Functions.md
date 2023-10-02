User-defined functions in `awk` allow you to create your own reusable blocks of code. This can be especially useful for encapsulating logic that you need to use in multiple places within your script.

**Syntax and structure**
```bash
function functionName(parameters) {
  # function body
}
```

**Basic Function Example**
```bash
BEGIN {
  function square(x) {
    return x * x;
  }

  print "The square of 4 is " square(4);
}
```

**Function with Multiple Parameters**
```bash
BEGIN {
  function area(length, width) {
    return length * width;
  }

  print "The area of a rectangle with length 4 and width 5 is " area(4, 5);
}
```

**Function Without a Return Value**
```bash
BEGIN {
  function greet(name) {
    print "Hello, " name "!";
  }

  greet("Alice");
}
```

#bash 