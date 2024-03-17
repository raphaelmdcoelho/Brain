They are executed before the controller or action is invoked, allowing additional checks or modify to authorization behaviour.

To implement a custom authorization filter, it's necessary to create a class that implements `IAuthorizationFIilter` or derives from the `AuthorizeAttribute` base class.

For example, you can create a custom authorization filter to check if the current user has a specific claim:

```csharp
public class ClaimAuthorizationFilter : IAuthorizationFilter
{
	private readonly string _claimType;
	private readonly string _claimValue;

	public ClaimAuthorizationFilter(string claimType, string claimValue)
	{
		_claimType = claimType;
		_claimValue = claimValue;
	}

	public void OnAuthorization(AuthorizationFilterContext context)
	{
		if(!context.HttpContext.User.HasClaim(_claimType, _claimValue))
		{
			context.Result = new ForbidResult();
		}
	}
}
```

There are two options to implement the custom authorization filter, you can either use it directly on a controller or action using the `[ServiceFilter]` attribute, or register it globally in your application's startup class:

```csharp
services.AddControllers(opt => 
{
	opt.Filters.Add(new ClaimAuthorizationFilter("Role", "Admin"));					   
});
```



#dotnet #authorization 