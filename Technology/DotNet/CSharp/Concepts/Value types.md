Value types comprise most built-in types (specifically, all `numeric` types, the `char` type, the `bool` type) as well custom `struct` and `enum` types.

The content of a value type variable or constant is simply a value. For example, ==the content of the built-in value type, int, is 32 bits of data==.

❗️==You can define a custom value type with the struct keyword==.

```csharp
public struct Point
{
	public int X;
	public int Y;
}
```

Or more tersely:

```csharp
public struct Point { public int X, Y; }
```

![[csharp_struct_01.png]]

The assignment of a value-type instance always copies the instance instead of the reference; for example:

```csharp
Point p1 = new Point();
p1.X = 7;

Point p2 = p1;

Console.WriteLine(p1.X); // 7
Console.WriteLine(p2.X); // 7

p1.X = 9;

Console.WriteLine(p1.X); // 9
Console.WriteLine(p2.X); // 7
```

![[csharp_struct_02.png]]

A value type cannot ordinarily have a null value:

```csharp
Point p = null; // Compile-time error
int x = null; // Compile-time error
```

#dotnet #csharp 