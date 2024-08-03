Specifies a temporary named result set, known as a common table expression ([[CTE]]). This clause can be used also in a create view statment.

## Boards

[[SQL-CTE-WITH.excalidraw]]

### Syntax

```sql
[ WITH <common_table_expression> [ ,...n ] ]

<common_table_expression>::=
    expression_name [ ( column_name [ ,...n ] ) ]
    AS
    ( CTE_query_definition )
```

* `WITH` keywork to define the start of the CTE.
* common_table_expression: Name of the CTE.  

```sql
WITH 
  CTE1 AS (
    SELECT id, name FROM table1 WHERE id < 5
  ),
  CTE2 AS (
    SELECT id, address FROM table2 WHERE id < 5
  )
SELECT CTE1.name, CTE2.address
FROM CTE1
JOIN CTE2 ON CTE1.id = CTE2.id;
```

```sql
WITH CTE1 AS (
  SELECT 1 AS id, 'Alice' AS name
)
SELECT name FROM CTE1;

```

#sqlserver #database 