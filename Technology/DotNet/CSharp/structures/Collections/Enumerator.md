A Enumerator is the object that actually does the iteration. It keeps track of the current position and knows how to move to the next element.

A high-level implementation:

```csharp
static void Main(string[] args)  
{  
	foreach (char c in "programmer")  
	Console.WriteLine(c);  
  
	Console.ReadKey();  
}
```

A low-level implementation:

```csharp
static void Main(string[] args)  
{  
	using (var enumerator = "programmer".AsEnumerable().GetEnumerator())  
	while (enumerator.MoveNext())  
	{  
		var element = enumerator.Current;  
		Console.WriteLine(element);  
	}  
  
	Console.ReadKey();  
}
```

#dotnet #csharp #collections