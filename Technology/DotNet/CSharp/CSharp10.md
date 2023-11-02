## C# 10:

### File-scoped namespaces.
### Global using directive.
### Implicit global using directive.
### Nondesteutive mutation for anonymous types using ***with*** Keyword.

```csharp
var a1 = { a = 1, b = 2 };
Var a2 = a1 with { c = 3 };
```

### New deconstruction  syntax:

```csharp
var point = (3, 5);
double x = 0;
(x, double y) = point;
```

### Field initializers and parameterless constructors in structs.
### Record struct:

```csharp
record struct Point (int x, int y);
```

### Lambda expressions enhanced:
* Implicit type (var) is permitted:
* An implicity type for a lambda expression is a Func or an Action, so in this case it should be a Func of a string.
* The parameters need to be explicitly state:
* A lambda expression can specify a return type:
* Now it's possible to apply attributes to lambda expressions:

```csharp
var result = () => "Hello world!";
```

```csharp
var square = (int x) => x * x;
```

```csharp
var sqr = int (int x) => x * x;
```

```csharp
Action a = [Description("test")] () => {};
```

### Nested property pattern:
* Old version:

```csharp
var obj = new Uri("https://...");
if(obj is Uri { Scheme.Lenght: 5 })...
```

* New version:

```csharp
if (obj is Uri { Scheme: { Lenght: 5}})...
```

#csharp #dotnet