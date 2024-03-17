
### Concepts

It relies on HTTP cookies to store the user's authentication information, such as a session ID or an encrypted token. The `cookie authentication middleware` handles the process of creating and validating cookies, allowing users to remain authenticated across multiple requests.

### Configuring Cookie Authentication

```csharp
services.AddAuthentication(CookieAuthenticationDefaults.AuthenticationScheme)
	.AddCookie(opt =>
	{
		opt.Cookie.Name = "MyAppCookie";
		opt.LoginPath = "/Account/Login";
	});
```

#dotnet #authentication #cookie
