## C# 8:

### Indices and ranges

* Indices and ranges simplify working with elements or portions of an array.
* Indices let you refer to elements relative to the end of an array by using the ^ operator. ^1 refers to the last element, ^2 refers to the second-to-last element, and so on.

```csharp
char[] vowels = new char[] {'a','e','i','o','u'}; 
char lastElement = vowels [^1]; // 'u'
char secondToLast = vowels [^2]; // 'o'
```

- Ranges let you “slice” an array by using the `..` operator:

```csharp
char[] firstTwo = vowels [..2];
char[] lastThree = vowels [2..];
char[] middleOne = vowels [2..3];
char[] lastTwo = vowels [^2..];
```

* C# has types Index and Range

```csharp
Index last = ^1; Range firstTwoRange = 0..2; char[] firstTwo = vowels [firstTwoRange]; // 'a', 'e'
```

* You can support indices and ranges in your own classes by defining an indexer with a parameter type of Index or Range:

```csharp
class Sentence {  string[] words = "The quick brown fox".Split();   public string this [Index index] => words [index];  public string[] this [Range range] => words [range]; }
```

### Using declarations

If you omit the brackets and statement block following a *using* statement, it becomes a *using declaration*. The resource is then disposed when execution falls outside the *enclosing* statement block:

```csharp
if (File.Exists ("file.txt"))
{
	using var reader = File.OpenText("file.txt");
	Console.WriteLine(reader.ReadLine());
}
```

### Read-only members

C# 8 lets you apply the *readonly* modifier to a struct's functions, ensuring that if the function attempts to modify any fields, a compile-time error is generated:

```csharp
struct Point
{
	public int X, Y;
	public readonly void ResetX() => X = 0;
}
```

If a *readonly* function calls a non-readonly function, the compiler generates a warning (and defensively copies the struct to avoid the possibility of a mutation).

### Static local methods

Adding the *static* modifier to a local method prevents it from seeing the local variables and parameters of the enclosing method. This helps to reduce coupling and enables the local method to declare variables as it pleases, without risk of colliding with those in the containing method.

### Default interface members

C# 8 lets you add a default implementation to an interface member, making it optional to implement:

```csharp
interface ILogger
{
	void Log(string text) => Console.WriteLine(text);
}
```

Default implementations must be called explicitly through the interface:

```csharp
((ILogger)new Logger()).Log("message");
```

Interfaces can also define static members (including fields), which can be accessed from code inside default implementations:

```csharp
interface ILogger
{
	void Log(string text) => Console.WriteLine(Prefix + text);
	static string PRefix = "";
}
```

Instance fields are prohibited.

### Switch expressions

From C# 8, you can use *[[switch]]* in the context of an expression:

```csharp
string cardName = cardNumber switch
{
	13 => "King",
	12 => "Queen",
	11 => "Jack",
	_ => "Pip card"_
};
```

### Tuple, positional, and property patterns

C# 8 supports three new patterns, mostly for the benefit of switch statements/expressions. *Tuple patterns* let you switch on multiple values:

```csharp
int cardNumber = 12;
suite - "spades";
string cardName = (cardNumber, suite) switch
{
	(13, "spades") => "King of spades",
	(13, "clubs") => "King of clubs",
	...
};
```

*Positional patterns* allow a similar syntax for objects that expose a deconstructor, and *property patterns* let you match on an object's properties. You can use all of the patterns both in switches and with the is operator. The following example uses a *property pattern* to test whether obj is a string with a length of 4.

```csharp
if(obj is string {Length: 4}) ...
```

### Nullable reference types

Whereas *nullable value types* bring nullability to value types, *nullable reference types* do the opposite and bring (a degree of) *non-nullability* to reference types, with the purpose of helping to avoid **NullReferenceExceptions**. Nullable reference types introduce a level of safety that's enforced purely by the compiler in the form of warnings or errors when it detects code that's at risk of generating a **NullReferenceException**. Nullable reference types can be enabled either at the project level (<mark>via the **Nullable** element in the .csproj project file</mark>) or in code (<mark>via the # nullable irective</mark>).
After it's enable, the compiler makes non-nullability the default: if you want a reference type to accept nulls, you must apply the ? suffix to indicate a *nullable reference type*:

```csharp
#nullable enable

string s1 = null; // Generates a compiler warning! (s1 is non-nullable)
string? s2 = null // Ok! s2 is nullable reference type
```

Uninitialized fields also generate a warning (if the type is not marked as nullable), as does dereferencing a nullable reference type, if the compiler thinks a **NullReferenceException** might occur:

```csharp
void Foo(string? s) => Console.Write(s.Length);
```

To remove the warning, you can use the *null-forgiving operator* (!):

```csharp
void Foo(string? s) => Console.Write(s!.Length);
```

### Asynchronous streams

Prior to C# 8, you could use *[[yield]]* return to write an *iterator*, or **await** to write an asynchronous function. But you couldn't do both and write an iterator that awaits, yielding elements asynchronously. C# 8 fixes this through the introduction of *asynchronous streams*:

```csharp
async IAsyncEnumerable<int> RangeAsync(int start, int count, int delay)
{
	for (int i = start; i < start + count; i++)
	{
		await Task.Delay(delay);
		yield return i;
	}
}
```

The **await foreach** statement consumes an asynchronous stream:

```csharp
await foreach (var number in RangeAsync(0, 10, 100))
	Console.WriteLine(number);
```

#csharp #dotnet