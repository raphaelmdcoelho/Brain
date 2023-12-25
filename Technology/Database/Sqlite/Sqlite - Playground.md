
### Starting container

```bash
dotnet run -it -v "$(pwd)||C:\:/workspace" -w /workspace keinos/sqlite3

docker stop "container_name"

docker rename "container_name" "new_container_name"

docker start "new_container_name"

docker exec -it "new_container_name" sh
```

### Initialize standalone process:

```sqlite
sqlite3 database_file
```

or

```sqlite
sqlite 3

.open ./database_name
```

### Operations

```sqlite
.help
.help TOPIC
```

**List databases**

```sqlite
.databases
```

**List tables**

```sqlite
.tables
```

**Checking table info**

```sqlite
PRAGMA table_info(table_name)
```

```sqlite
create table category(
	id integer primary key,
	name varchar(100)
);

create table product(
	id integer primary key,
	label varchar(100),
	category_id integer,
	foreign key (category_id) references category (id) 
);

PRAGMA foreign_keys;
PRAGMA foreign_keys = ON;
```

```sqlite
insert into category (name) values ('beverage');

insert into product values (1, 'orange juice', 1);

insert into product values select * from product2;
```

```sqlite
update product
set label = 'strawberry juice'
where id = 1;
```

```sqlite
delete from product where id = 1;
```

```sqlite
.mode box --wrap 30
.eqp yes
.changes

select * from product;
```

```sqlite
.backup main new_backup_name
```

```sqlite
.show
.schema

PRAGMA integrity_check
```

```sqlite
alter table product2
rename to product3;

drop table product3;
```

```sqlite
select * from product p
inner join category c
on c.id = p.category_id
where c.id = 2;
```

```sqlite
.print "some text"
```

```sqlite
.quit
```

#sqlite #database 