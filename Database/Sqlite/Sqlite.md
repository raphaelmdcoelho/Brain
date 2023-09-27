- Sqlite project provides a simple [[Command-line program]] named sqlite3 that allows user to manually enter and execute SQL statements against an Sqlite database.
- It's possible to add it to **Path** environment variable to use it *global*.

## Create database

```
Sqlite3 ex1
```

## Create table

```
sqlite> create table tbl1(one text, two int);
```

## Insert

```
sqlite> insert into tbl1 values('hello', 10);
```

## Select

```
select * from tbl1;*
```

## Management

- Terminate sqlite3 by typing your system [[End-Of-File]] character (Ctrl-D)
- Use interrupt character (Ctrl-C) to stop a long-runnung SQL statment.

## Special commands

- [[dot-commands]]

#sqlite 


