
Assemblies are fundamental units of deployment, version control, reuse, activation scoping, and security permissions for .NET-based applications. An assembly is a collection of types and resources that are built to work together and form a logical unit of functionality. Assemblies take the form of executable (.exe) or Dynamic Link Library (.dll) files, and are the building blocks of .NET applications. They provide the common language runtime with the information it needs to be aware of type implementations.

Assemblies have the following properties:

* Assemblies are implemented as .exe or .dll file.
* For libraries that target .NET framework, you can share assemblies between applications by putting them in the global assembly cache (GAC). You must strong-name assemblies before you can include them in the GAC.
* Assemblies are only loaded into memory if they're required. If they aren't used, they aren't loaded. Therefore, assemblies can be an efficient way to manage resources in larger projects.
* You can programmatically obtain information about an assembly by using Reflection.
* You can load an assembly just to inspect it y using the `MetadataLoadContext` class on .NET and .NET Framework. `MetadataLoadContext` replaces the `Assembly.ReflectionOnlyLoad` methods.

#csharp #dotnet 