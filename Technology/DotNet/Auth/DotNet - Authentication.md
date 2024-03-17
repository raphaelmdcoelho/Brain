
### Concepts

It's the process of check `who you are claiming to be` or `who you are`. The authentication process is responsible to check your IDENTITY.

**Authentication Scheme**

It represents a specific `method` or `protocol` used to authenticate users.

Authentication in ASP.NET Core revolves around the concept of `authentication schemes`:
* cookie.
* jwt bearer.
* external auth (OAuth and OpenID).

Authentication schemes are `registered` in the application's startup class using the `AddAuthentication` method. This method allows you to specify one or more authentication schemes and their respective options.

```csharp
services.AddAuthentication(CookieAuthenticationDefaults.AuthenticationScheme)
	.AddCookie(opt => 
	{
		// Configure cookie options
	})
```

### [[DotNet - Cookie Authentication]]

### [[DotNet - Claim-Based Authentication]]

### [[DotNet - External Authentication Providers]]

### [[DotNet - JWT Bearer Authentication]]

#dotnet #authentication 