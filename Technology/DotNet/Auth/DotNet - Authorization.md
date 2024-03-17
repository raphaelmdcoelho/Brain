
Is the process responsible to check what actions a user is allowed to perform whitin an application.

Authorization in ASP.NET Core is primarily controlled through the use of the [Authorize] attribute.

This is a example of use of this attribute. Here the user is allowed to interact with the action, only if it has a admin role: 
```csharp
[Authorize(Roles = "Admin")]
```

**Authorization policies**

```csharp
services.AddAuthorization(options =>  
{  
	options.AddPolicy("AdminOnly", policy =>  
	{  
		policy.RequireRole("Admin");  
	});  
});
```

On the above example, it is possible to configures the authorization process in a controller/action through the following attribute:

```csharp
[Authorize(Policy = "AdminOnly")]
```

Authorization policies can also be based on other factors, such as claims, custom requirements, or a combination of conditions. This allows you to implement complex access control logic based on various user attributes or application-specific rules.

### [[DotNet - Role-Based Authorization]]

#dotnet #authorization 