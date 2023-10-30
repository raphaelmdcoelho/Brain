
```sql
MERGE 
    dbo.Destiny AS Destiny
USING 
    dbo.Origin AS Origin ON (Origin.Id = Destiny.Id)

WHEN MATCHED THEN
    UPDATE SET 
        Destiny.Date = Origin.Date,
        Destiny.Name = Origin.Name

WHEN NOT MATCHED THEN
    INSERT
    VALUES(Origin.Id, Origin.Date, Origin.Name);
```

#sqlserver #database 