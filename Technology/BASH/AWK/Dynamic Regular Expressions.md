Dynamic Regular Expressions in `awk` allow you to use variables as patterns in your regular expression matching. This flexibility can be especially useful when you need to generate or change the pattern at runtime.

### Concept and Benefits
In `awk`, you generally use `/pattern/` for regular expression matching. However, if you want to use a variable to store the pattern, that's when dynamic regular expressions come into play. They enable you to match text based on patterns stored in variables, which can be changed during the program's execution.

### Examples 

**Basic Example**
```bash
BEGIN {
  pattern = "apple";
  text = "I have an apple.";

  if (text ~ pattern) {
    print "Match found!";
  }
}
```

**Changing Pattern Dynamically**
```bash
BEGIN {
  fruits[1] = "apple";
  fruits[2] = "banana";
  fruits[3] = "cherry";

  text = "I have an apple and a banana.";

  for (i in fruits) {
    pattern = fruits[i];
    if (text ~ pattern) {
      print "Found " pattern " in the text!";
    }
  }
}

```

**#### Case-insensitive Matching**
```bash
BEGIN {
  pattern = "apple";
  text = "I have an Apple.";

  ignoreCasePattern = tolower(text);
  if (tolower(text) ~ ignoreCasePattern) {
    print "Case-insensitive match found!";
  }
}
```




#bash #awk