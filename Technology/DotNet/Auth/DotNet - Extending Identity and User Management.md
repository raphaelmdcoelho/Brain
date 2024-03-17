You can extend the default identity system by creating custom user and role classes that inherit from the built-in `IdentityUser` and `IdentityRole` classes.

```csharp
public class ApplicationUser: IdentityUser
{
	public string FullName { get; set; }
	public DateTime BirthDate { get; set; }
}
```

To use this custom class, it's necessary to update the application DbContext to included it:

```csharp
public class ApplicationDbContext : IdentityDbContext<ApplicationUser>
{
	// DbContext configuration
}
```

In addition to extending the identity system, you can also customize the user management and role management functionality by implementing custom user stores and role stores. This allows you to store user and role data in different data sources or integrate with existing user management systems.

#dotnet #authentication #authorization