Built-in functions in `awk` offer a range of pre-defined functionalities that assist with text manipulation, arithmetic calculations, and other common tasks. These functions come as a standard part of the `awk` language, so you don't need to define them yourself.

### Categories of Built-in Functions

1. String Functions (e.g., `length`, `substr`, `index`)
2. Numeric Functions (e.g., `sin`, `cos`, `int`)
3. Time Functions (e.g., `systime`, `strftime`)
4. Miscellaneous Functions (e.g., `rand`, `srand`)

### Examples for Each Category

**String Functions**
```bash
BEGIN { print length("Hello"); }  # Output: 5

BEGIN { print substr("Hello", 2, 2); }  # Output: "el"
```

**Numeric Functions**
```bash
BEGIN { print int(4.9); }  # Output: 4

BEGIN { print sqrt(16); }  # Output: 4
```

**Time Functions**
```bash
BEGIN { print systime(); }

BEGIN { print strftime("%Y-%m-%d", systime()); }
```

**Miscellaneous Functions**
```bash
BEGIN { print rand(); }

BEGIN { srand(systime()); print rand(); }
```

#bash #awk