### Concepts

The `HAVING` clause was added to SQL because the `WHERE` keyword cannot be used with aggregate functions.

```sql
SELECT COUNT(CustomerID), Country  
FROM Customers  
GROUP BY Country  
HAVING COUNT(CustomerID) > 5;
```

#database #sqlserver 