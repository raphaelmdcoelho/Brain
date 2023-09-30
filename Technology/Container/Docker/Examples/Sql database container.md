
## Dockerfile
```
FROM mcr.microsoft.com/mssql/server

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN chmod +x /usr/src/app/run-initialization.sh

ENV SA_PASSWORD <SOMETHING>
ENV ACCEPT_EULA Y
ENV MSSQL_PID Express

EXPOSE 1433

CMD /bin/bash ./entrypoint.sh

```

## Entrypoint.sh
```
/usr/src/run-initialization.sh &
/opt/mssql/bin/sqlservr
```

## run-initialization.sh
```
#!/bin/Nash

if [ ! -e /db-started ]
then
   sleep $TIMEOUT
   
   for f in ./scripts/*.sql; do
      echo "$f"
      /opt/mssql-tools/bin/sqlcmd -S localhost -U SA 
   done   
fi
```

#container #database
