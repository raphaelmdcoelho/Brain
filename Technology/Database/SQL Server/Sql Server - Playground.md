
### Pull image

```powershell
docker pull mcr.microsoft.com/mssql/server:2022-latest
```

### Run container

```powershell
docker run \ 
-e "ACCEPT_EULA=Y" \
-e "MSSQL_SA_PASSWORD=SqlServer2023*" \
-p 1433:1433 \
--name sqldatabase \
--hostname sqldatabase \
-d \
mcr.microsoft.com/mssql/server:2022-latest
```

### Connect to container

```powershell
docker exec -it sqldatabase "bash"
```

### Connect locally with `sqlcmd`

```powershell
/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "SqlServer2023*"
```


### Create and query data

```sql
CREATE DATABASE TestDB;

SELECT Name from sys.databases;

GO

USE TestDB;

QUIT
```

### Connecting outside the container

```powershell
sqlcmd -S <ip_address>,1433 -U SA -P "<YourNewStrong@Passw0rd>"
```

#sqlserver #database 