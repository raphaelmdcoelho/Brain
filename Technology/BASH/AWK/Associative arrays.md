An associative array in `awk` is defined implicitly—meaning you don't have to explicitly declare the array before using it. You can add key-value pairs simply by assigning a value to a specific key.

**Basic structure**

```
arrayName["key"] = value
```

**Initializing and Populating an Array**
```bash
BEGIN {
  ages["Alice"] = 30;
  ages["Bob"] = 40;
  ages["Charlie"] = 25;
}
```

**Accessing Values by Keys**
```bash
BEGIN {
  ages["Alice"] = 30;
  print "Alice's age is " ages["Alice"];
}
```

**Iterating Through an Array**
```bash
BEGIN {
  ages["Alice"] = 30;
  ages["Bob"] = 40;
  ages["Charlie"] = 25;

  for (name in ages) {
    print "Name: " name ", Age: " ages[name];
  }
}
```

**Note**: Here the ***for in*** is retrieving the name of the property.

**Deleting Key-Value Pairs**
```bash
BEGIN {
  ages["Alice"] = 30;
  delete ages["Alice"];
}
```

#bash 