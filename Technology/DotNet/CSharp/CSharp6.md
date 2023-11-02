C# 6.0, which shipped with Visual Studio 2015, features a new-generation compiler, completely written in C#. Known as project "[[Roslyn]]", the new compiler exposes the entire compilation pipeline via libraries, allowing you to perform code analysis on arbitraty source code. The compiler itself is open source, and the source code is available at https://github.com/dotnet/roslyn.

### Null-Conditional operator ("Elvis")

Avoids having to explicitly check for null before calling a method or accessing a type member. In the following example, `result` evaluates to null instead of throwing a `NullReferenceException`:

```csharp
System.Text.StringBuilder sb = null;
string result = sb?.ToString();
```

### Expression-bodied functions

Allow methods, properties, operators, and indexers that comprise a single expression to be written more tersely, in the style of a lambda expression:

```csharp
public int TImesTwo (int x) => x * 2;
public string SomeProperty => "PRoperty value";
```

### Property initializers

Let you assign a initial value to an automatic property:

```csharp
public DateTime TimeCreated { get; set; } = DateTime.Now;
```

❗️Initialized properties can also be read-only:

```csharp
public DateTime TimeCreated { get; } = DateTime.Now;
```

### Read-only properties initialization

Now read-only properties can also be set in the constructor, making it easier to create immutable (read-only) types.

### Index initializers

Allow single-step initialization of any type that exposes an [[Indexer]]:

```csharp
var dict = new Dictionary<int, string>()
{
	[3] = "three",
	[10] = "ten"
}
```

### String interpolation

Offers a succinct alternative to ==string.Format==:

```csharp
string s = $"It is {DateTime.Now.DayOfWeek} today";
```

### Exception filters

Let you apply a condition to a catch block:

```cshap
string html;
try
{
	html = await new HttpClient().GetStringAsync("http://asef");
}
catch (WebException ex) when (ex.Status == WebExceptionStatus.Timeout)
{
	...
}
```

### Static using

The using static directive lets you import all the static members of a type so that you can use those members unqualified:

```csharp
using static System.Console;
...
WriteLine("Hello, world");
```

### Nameof

The `nameof` operator returns the name of a variable, type, or other symbol as a string. This avoids breaking code when you rename a symbol in Visual Studio.

```csharp
int capacity = 123;
string x = nameof(capacity);
string y = nameof(Uri.Host);
```

#csharp #dotnet