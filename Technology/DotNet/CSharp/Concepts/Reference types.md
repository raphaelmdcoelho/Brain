Reference types comprise all `class`, `delegate`, and `interface types`. (This includes the predefined `string` type).
The fundamental difference between value types and reference types is how they are handled in memory.

A reference type is more complex than a value type, having two parts: an `object` and the `reference` to that object. Th content of a reference-type variable or constant is a reference to an object that contains the value. Here is the Point type from our previous example rewritten as a class rather than a struct:

```csharp
public class Point
{
	public int X, Y;
}
```

![[reference_type_01.png]]

Assigning a reference-type variable copies the reference, not the object instance. This allows multiple variables to refer to the same object - something not ordinarily possible with value types. If we repeat the previous example, but with Point now a class, an operation to p1 affect p2:

```csharp
Point p1 = new Point();
p1.X = 7;

Point p2 = p1; // Copies p1 reference

Console.WriteLine(p1.X); // 7
Console.WriteLine(p2.X); // 7

p1.X = 9;

Console.WriteLine(p1.X); // 9
Console.WriteLine(p1.X); // 9
```

Shows that p1 and p2 are two references that point to the same object.

![[reference_type_02.png]]

### Null

A reference can be assigned the literal `null`, indicating that the reference points to no object:

```csharp
Point p = null;
Console.WriteLine(p == null); // True
```

C# also has a construct called `nullable value types` for representing value-type nulls.

#dotnet #csharp 