- .backup ?DB? FILE
- .changes on|off ==> *shows number of rows changed by a SQL*
- .databases
- eqp on|off|full|... ==> *automatic EXPLAIN QUERY PLAN*
- .excel ==> *display output of next query command in spreadsheet*
- .import FILE TABLE ==> *import a data from a file into a table*
- .tables ?TABLE?

### Examples

**Show databases**

```sqlite
.databases
```

**Show tables**

```sqlite
.tables
```

```sqlite
SELECT name FROM sqlite_schema
WHERE type IN ('table','view') AND name NOT LIKE 'sqlite_%'
ORDER BY 1
```
### Save a new database

```sqlite
.save database_name;
```

### Output formats

* [[Sqlite - Output Formats]]

### Schema

```sqlite
.schema

.schema main.*

.schema --indent
```

```sqlite
.schema table_name

SELECT sql FROM sqlite_schema
ORDER BY tbl_name, type DESC, name
```

### Output

By default, sqlite3 sends query results to standard output. But it's possible to change this.

```sqlite
.output file.txt
select * from table;
```

using these statements a file will be generated as result with the content of query result. This will work for all queries after.

To change output stdout of query result only one time is possible by using `once`

```sqlite
.once file.txt
```

Using sh commands

```sqlite
.once | grep 'some_word'
.output | grep 'some_word'
```

Send output to a file or spreadsheet

```sqlite
.once -e
.once -x
```

The command `.excel` is a alias for `.once -x` doing the same thing.

### Reading SQL from file

In interactive mode, sqlite3 read input text (either SQL commands and dot-commands) from keyboard but it's possible to redirect input.

```sqlite
.read script.sql
```

```sqlite
.read | script-generator.bat
```

### Importing CSV files or other formats as tables

```sqlite
.import --csv --skip 1 --schema temp C:/folder/file_name.csv table_name
```

### Export to CSV

```sqlite
.headers on
.mode csv
.once c:/folder/file_name.csv
select * from table_name;
# windows version
.system c:/folder/file_name.csv
# linux version
.system xdg-open file_name.csv
```

### Load extensions 

```sqlite
.load /path/extension_name
```

### Index recommendations

```sqlite
.expert
select * from table_name;
```

#sqlite #database 
