When you prefix a `using` directive with the global keyword, it applies the directive to all files in the project:

```csharp
global using System;
global using System.Collection.Generic;
global using Console=Spectre.Console.AnsiConsole;
global using static System.Console;
```

This lets you avoid repeating the same directive in every file. global using directives work with using static.

==It's possible to add a new file like `Using.cs` and add all global using there==.

Additionally, .NET 6 projects now support implicit global using directives: if the `ImplicitUsings` element is set to true in the project file, the most commonly used namespaces are automatically imported (based on the SDK project type).

```xml
<ItemGroup> <ImplicitUsing Include="System.Xml.Linq" /> <ImplicitUsing Remove="System.IO" /> </ItemGroup>
```

```xml
<ImplicitUsings>disable</ImplicitUsings>
```

You can even go one step further, and define a `GlobalUsing.Tests.cs` with all the test-relevant namespaces, and create a `Directory.Build.props` in the **root of your repository**. This will let those namespaces be [automatically imported](https://docs.microsoft.com/en-us/visualstudio/msbuild/customize-your-build?view=vs-2019#directorybuildprops-and-directorybuildtargets) in every project ending with the `Tests` postfix:

```xml
<Project>
	<ItemGroup Condition="$(MSBuildProjectName.EndsWith('Tests'))">
		<Compile Include="GlobalUsings.Tests.cs" />
	</ItemGroup>
</Project>
```

```xml
<Project>
	<ItemGroup Condition="$(MSBuildProjectName.EndsWith('Tests'))">
		<PackageReference Include="FluentAssertions" Version="6.1.0" />
		<Using Include="FluentAssertions" />
	</ItemGroup>
</Project>

<Project>
	<ItemGroup>
		<Using Include="System.Math" Static="True" />
		<Using Include="Spectre.Console.AnsiConsole" Alias="Console" />
	</ItemGroup>
</Project>

<Project>
	<ItemGroup>
		<PackageReference Include="Package.With.UnwantedNamespace" />
		<Using Remove="UnwantedNamespace" />
	</ItemGroup>
</Project>
```

#csharp #dotnet 