
## How to use


**Configuration**
```csharp
var serviceProvider = new ServiceProvider()
	.AddHttpClient()
	.BuildServiceProvider();
```

**Implementation**
```csharp
var httpCLientFactory = serviceProvider
	.GetService<IHttpClientFactory>();

var client = httpClientFactory.CreateClient();

await client.GetFromJsonAsync("http://www.google.com");
await client.GetStringAsync("http://www.google.com");
```

#technology #computing #dotnet 