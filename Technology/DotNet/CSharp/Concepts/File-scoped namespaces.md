File scoped namespaces use a less verbose format for the typical case of files containing only one namespace. The file scoped namespace format is `namespace X.Y.Z;` (note the semicolon and lack of braces). This allows for files like the following:

```csharp
namespace X.Y.Z;

using System;

class X
{
}
```

#csharp #dotnet 