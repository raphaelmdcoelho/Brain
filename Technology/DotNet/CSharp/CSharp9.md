## C# 9:

### Top-level statements:
* Ability to run a code without a Main method and a Program class.
* Magic args variable.
### Init-only setters:
* A property can be declared using the ***init*** keyword instead of ***set***.
* It creates a immutable read-only type that can be populated via an object initializer instead of a constructor.
* It allows nondestructive mutation when used in records.
```csharp
public string Text { get; init; }

var text1 = new Class { Text = "Message" };

var text2 = text1 with { OtherProperty = value }
```
### [[Records]]
* It's a class that word good with immutable data.
* Allows nondestructive mutation.
* With records is possible to eliminate the properties boilerplate.
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

### Pattern-matching improviments:
* The relational pattern allows operators to appers in patters. So now with **patter combinators** you can combine patterns via threenl new keywords (and, or and not):

```csharp
string GetWeightCategory (decimal bmi) => bmi Switch
{
	<= 18.5m => "underweight",
	> 25m => "normal",
	> 30m => "overweight",
	_ => "obese"
};
```

```csharp
var isVowel (char letter) => letter is 'a' or 'e' or 'i' or 'o' or 'u';
```

### Target-typed new expressions
* When constructing an object, C# 9 lets you omit the type name when the compiler can infer it unambiguously:

```csharp
StringBuilder message = new("");
```

#csharp #dotnet