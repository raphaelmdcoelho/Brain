
### Concepts

**Claim**

A claim represents a piece of information about the user, such as their name, email address, or role.

By using claims, you can easily extend the user's identity with additional data and make authorization decisions based on these claims.

In ASP.NET Core, claim-based authentication is implemented using the `ClaimsIdentity` and `ClaimsPrincipal` classes.
*  The `ClaimsIdentity` represents a collection of claims associated with a user.
* The `ClaimsPrincipal` represents the user's identity as a whole.

When a user is authenticated, their claims are stored in a `ClaimsPrincipal`, which is then attached to the current request's `HttpContent.User` property.

```csharp
var claims = new List<Claim>
{ 
	new Claim(ClaimTypes.Name, "John Doe")
};

var identity = new ClaimsIdentity(claims, "MyAuthenticationScheme");

var principal = new ClaimsPrincipal(identity);

await HttpContext.SignInAsync(principal);
```

#dotnet #authentication #claim-based-auth
