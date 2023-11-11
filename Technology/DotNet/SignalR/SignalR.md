### Concepts

SignalR work with hubs.

```csharp
// Server
using Microsoft.AspNetCore.SignalR;

builder.Services.AddSignalR();

app.MapHub<MyHub>("/chat");

class MyHub : Hub
{
	public async IAsyncEnumerable<DateTime> Streaming(CancellationToken cancellationToken)
	{
		while(true)
		{
			yield return DateTime.Now;
			await Task.Delay(1000, cancellationToken);
		}
	}
}
```

```csharp
// Client
using Microsoft.AspNetCore.SignalR.Client;

const string url = "https://localhost:5001/chat";

await using var connection = new HubConnectionBuilder()
.WithUrl(url)
.Build();

await connection.StartAsync();

await foreach(var date in connection.StreamAsync<DateTime>("Steaming"))
{
	Console.WriteLine(date);
}
```
#dotnet