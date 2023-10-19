
### Use in unit tests
```csharp
var options = new DbContextOptionsBuilder<CustomDbContext>
	.UseInMemoryDatabase(databaseName: "Name")
	.Options;

var context =  new CustomDbContext(options);
var _subject = new PayerContractRepository(context);
```

#dotnet #csharp #orm 