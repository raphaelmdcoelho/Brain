### Concepts

It's used to import data from a flat file into a sql server table.

### Commands

```sql
BULK INSERT PRODUCT
FROM 'file_name.txt'
```

### Parameters

* **CODEPAGE**: Specifies punctuation.
* **MAXERRORS**: max errors can happens during import.
* **FIELDTERMINATOR**: character used to separete columns. The default value is TAB (/t).
* **ROWTERMINATOR**: character used to separete rows. The default value is ENTER (/n).
* **KEEP_IDENTITY**: disables auto identity.
* **FORMATFILE**: file format used as source data.
* **FIRSTROW**: defines first row to be imported.
* **LASTROW**: defines last row to be imported.

```sql
BULK INSERT PRODUCT 
FROM ‘C:\PRODUCTS.TXT’ 
WITH ( 
	FORMATFILE=‘C:\PRODUTOSTAB.FMT’,
	CODEPAGE=‘ACP’, MAXERRORS = 0,
	FIRE_TRIGGERS, FIRSTROW = 1, 
	LASTROW = 10 
)
```

#sqlserver #database 
