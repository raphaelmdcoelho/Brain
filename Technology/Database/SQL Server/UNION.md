### Concepts

The `UNION` operator is used to combine the result-set of two or more `SELECT` statements.

- Every `SELECT` statement within `UNION` must have the same number of columns
- The columns must also have similar data types
- The columns in every `SELECT` statement must also be in the same order

### Usage

```sql
SELECT _column_name(s)_ FROM _table1_  
UNION  
SELECT _column_name(s)_ FROM _table2_;
```

The `UNION` operator selects only distinct values by default. To allow duplicate values, use `UNION ALL`:

```sql
SELECT _column_name(s)_ FROM _table1_  
UNION ALL  
SELECT _column_name(s)_ FROM _table2_;
```


#database #sqlserver 