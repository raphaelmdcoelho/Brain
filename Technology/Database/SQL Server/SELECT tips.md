- To add simple quotes and a command to each value from a select statment it's possible to use concat function:
```sql
SELECT CONCAT('''', column_name, '''', ',') FROM table_name;
```

#sqlserver #database 