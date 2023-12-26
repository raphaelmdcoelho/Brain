**Checking actual mode**

```sqlite
.mode
```

**Changing row separator**

```sqlite
.mode list

.separator ", "
```

**Sql literals**

```sqlite
.mode quote
```

**Line mode**

```sqlite
.mode line
```

**Columnar modes**

* Column mode

```sqlite
.mode column

.width 15 0 -7
```

**Note**: zero means auto adjust and negative sign means right-justify.

* Box

```sqlite
.mode box
```

```sqlite
.mode qbox
```
**Note**: represents this whole command: `mode box --wrap 60 --quote`

* Table

```sqlite
.mode table
```

* Markdown

* Another options for columnar modes

**wrap** : causes columns to wrap text that is no longer than N characters.
```sqlite
--wrap N
```

**wordwrap**: same as above, but for words.
```sqlite
--wordwrap N || -ww N
```

**quote**: 
```sqlite
--quote
```

**Mode Insert**

**Mode CSV**

**Mode JSON**

**Mode TCL**



#sqlite #database 