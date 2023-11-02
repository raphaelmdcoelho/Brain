### Concepts


### Usage

**Adding a primary key**

```sql
ALTER TABLE table_name ADD CONSTRAINT constraint_name PRIMARY KEY
 (col1, col2);

```

**Adding a foreign key**

```sql
ALTER TABLE orders ADD CONSTRAINT users_fk FOREIGN KEY (user_id) REFERENCES
 users (user_id);

```

** Adding unique constrain**

```sql
ALTER TABLE users ADD CONSTRAINT email_unique UNIQUE
 (email);

```

**Adding a check constrain**

```sql
ALTER TABLE orders ADD CONSTRAINT check_revenue_positive CHECK (revenue >= 0);

```

**Dropping a constraint

```sql
ALTER TABLE table DROP CONSTRAINT constraint_name;
```

#database #sqlserver 