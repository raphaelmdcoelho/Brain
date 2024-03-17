### Concepts

```csharp
services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)  
	.AddJwtBearer(options =>  
	{  
		options.TokenValidationParameters = new TokenValidationParameters  
		{  
			ValidateIssuer = true,  
			ValidateAudience = true,  
			ValidateIssuerSigningKey = true,  
			ValidIssuer = "YOUR_ISSUER",  
			ValidAudience = "YOUR_AUDIENCE",  
			IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes("YOUR_SIGNING_KEY"))  
		};  
	});
```

**Issuer**
It is responsible for creating and signing the token.
The issuer's identity (specified by `ValidIssuer`) is included in the token, allowing the recipient to verify that the token comes from a trusted source.

**Audience**
The **audience** is intended to prevent the token from being used by unauthorized parties.

#dotnet #authentication #jwt
