## C# 10:

1. File-scoped namespaces.
2. Global using directive.
3. Implicit global using directive.
4. Nondesteutive mutation for anonymous types using ***with*** Keyword.

```csharp
var a1 = { a = 1, b = 2 };
Var a2 = a1 with { c = 3 };
```

5. New deconstruction  syntax:

```csharp
var point = (3, 5);
double x = 0;
(x, double y) = point;
```

6. Field initializers and parameterless constructors in structs.
7. Record struct:

```csharp
record struct Point (int x, int y);
```

8. Lambda expressions enhanced:
	1. Implicit type (var) is permitted:
	2. An implicity type for a lambda expression is a Func or an Action, so in this case it should be a Func of a string.
	3. The parameters need to be explicitly state:
	4. A lambda expression can specify a return type:
	5. Now it's possible to apply attributes to lambda expressions:

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

9. Nested property pattern:
	1. Old version:
	2. New version:
```csharp
var obj = new Uri("https://...");
if(obj is Uri { Scheme.Lenght: 5 })...
```

```csharp
if (obj is Uri { Scheme: { Lenght: 5}})...
```

## C# 9:

1. Top-level statements:
	1. Ability to run a code without a Main method and a Program class.
	2. Magic args variable.
2. Init-only setters:
	1. A property can be declared using the ***init*** keyword instead of ***set***.
	2. It creates a immutable read-only type that can be populated via an object initializer instead of a constructor.
	3. It allows nondestructive mutation when used in records.
```csharp
public string Text { get; init; }

var text1 = new Class { Text = "Message" };

var text2 = text1 with { OtherProperty = value }
```
3. [[Records]]
		1. It's a class that word good with immutable data.
		2. Allows nondestructive mutation.
		3. With records is possible to eliminate the properties boilerplate.
```csharp
record Point 
{  
	public Point (double x, double y) => (X, Y) = (x, y);   
	public double X { get; init; }  
	public double Y { get; init; } 
}
```

```csharp
record Point (double X, double Y);
```

4. Pattern-matching improviments:
	1. Operators can apper in patters.
```csharp
string GetWeightCategory (decimal bmi) => bmi Switch
{
	<= 18.5m => "underweight",
	> 25m => "normal",
	> 30m => "overweight",
	_ => "obese"
};
```

#dotnet #csharp
