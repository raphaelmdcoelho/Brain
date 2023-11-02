
### Readonly structs

Enforces that all fields are readonly, to aid in declaring intent and to allow the compiler more optimization freedom:

```csharp
readonly struct Point
{
	public readonly int X, Y; // X and Y must be readonly
}
```

### Numeric literal improvements

Numeric literals in C# 7 can include underscores to improve readability. This are called *digit separators* and are ignored by the compiler:

```csharp
int million = 1_000_000;
```

*Binary literals* can be specified with the 0b prefix:

```csharp
0b1010_1011_1100_1101_1110_1111;
```

### Out variables and discards

C#7 makes it easier to call methods that contain out parameters. First, you can now declare out variables on the fly.

```csharp
bool successful = int.TryParse("123", out int result);
Console.WriteLine(result);
```

❗️==And when calling a method with multiple out parameters you can discard ones youre uninterested in with the underscode character.==

```csharp
SomeBigMethod(out _, out _, out _, out int x, out _, out _, out _);
Console.WriteLine(x);
```

### Type patterns and pattern variables

You can also introduce variables on the fly with the is operator. There are called pattern variables.

```csharp
void Foo(object x)
{
if(x is string s)
	Console.WriteLIne(s.Length);
}
```

❗️The switch statement also supports type patterns, so you can switch on type as well as constants. You can specify conditions with a ==when== clause and also switch on the null value:

```csharp
switch(x)
{
case int i:
	Console.WriteLine("It's an int!");
	break;
case string s:
	Console.WriteLine(s.Length);
	break;
case bool b when b == true:
	Console.WriteLine("True");
	break;
case null:
	Console.WriteLine("Nothing");
	break;
}
```

### Local methods

❗️A *local method* is a method declared within another function.

```csharp
void WriteCubes()
{
	Console.WriteLine(Cube (3));
	Console.WriteLine(Cube (4));
	Console.WriteLine(Cube (5));

	int Cube (int value) => value * value * value;
}
```

**More expression-bodied members**

C# 6 introduced the expression-bodied =="fat-arrow"== syntax for methods, read-only properties, operators, and indexers. C# 7 extends this to constructors, read/write properties and finalizers:

```csharp
public class Person
{
	string name;
	public Person (string name) => Name = name;

	public string Name
	{
		get => name;
		set => name = value ?? "";
	}
	~Person () => Console.WriteLIne("finalize");
}
```

note: the symbol `~` here in the example above, is creating a [[Finalizers - Destructors]].

### Deconstructors

C# 7 introduces the deconstructor pattern. ==Whereas a constructor typically takes a set of values (as parameters) and assigns them to fields, a deconstructor does the reverse and assigns fields back to ta set of variables==. We could write a deconsructor for the Person class in the preceding example as follows (exception handling aside):

```csharp
public void Deconstruct(out string firstName, out string lastName)
{
	int spacePos = name.IndexOf(' ');
	firstName = name.Substring(0, spacePos);
	lastName = name.Subsring(spacePos + 1);
}
```

Deconstructors are called with the following special syntax:

```csharp
var joe = new Person("Joe Bloggs");
var (first, last) = joe; // Deconstruction
Console.WriteLine(first);
Console.WriteLine(last);
```

### Tuples

Perhaps the most notable improvement to C# 7 is explicit tuple support. Tuples provide a simple way to store a set of related values:

```csharp
bar bob = ("Bob", 23);
Console.WriteLine("bob.Item1");
Console.WriteLine("bob.Item2");
```

❗️C#'s new tuples are syntactic sugar for using the ==<System.ValueTuple<...>== generic structs. But thanks to compiler magic, tuple elements can be named:

```csharp
var tuple = (name: "Bob", age: 23);
Console.WriteLine(tuple.name);
Console.WriteLine(tuple.age);
```

❗️With tuples, functions can return multiple values without resorting to out parameters or extra type baggage:

```csharp
static (int row, int column) GetFIlePosition() => (3, 20);

static void Main()
{
	var pos = GetFilePosition();
	Console.WriteLine(pos.row);
	Console.WriteLine(pos.column);
}
```

❗️Tuples implicitly support the deconstruction pattern, so you can easily deconstruct them into individual variables:

```csharp
static void Main()
{
	(int row, int column) = GetFilePosition();
	Console.WriteLine(row);
	Console.WriteLine(column);
}
```

### Throw expressions

==Prior to C# 7, throw was always a statement. Now it can also appear as an expression in expression-bodied functions:==

```csharp
public string Foo() => throw new NotImplementedException();
```

#csharp #dotnet