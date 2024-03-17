### Concepts

To enable external authentication, you need to configure the desired authentication provider and register it in your application's startup class. This involves obtaining the necessary `client IDs` and `secrets` from the provider's developer portal and specifying them in the authentication options.

```csharp
services.AddAuthentication()
	.AddGoogle(opt => 
	{
		opt.ClientId = "";
		opt.ClientSecret = "";
	})
```

#dotnet #authentication #external-authentication-provider
