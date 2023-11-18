### Concepts

A iterator is a method, property or index that allows you to use `foreach` loops on collections.

An iterator is a construct in C# that allows for traversing through a collection (like arrays, lists) in a controlled way. It’s often implemented as a method, property, or indexer.

As the enumeration of subsequent elements of the collection is not very convenient and readable using the **GetEnumerator()** method, so something like iterators was created, thanks to them we do not need to use such methods as eg **MoveNext()** or **GetEnumerator()**, iterators use only yield return words used to return values from a loop.

```csharp
static void Main(string[] args)  
{  
	foreach (char fib in Programmer("programmer"))  
	Console.Write(fib + " ");  
  
	Console.ReadKey();  
}  
  
static IEnumerable<char> Programmer(string couplechars)  
{  
	for (int i = 0; i < couplechars.Length; i++)  
	{  
		yield return couplechars[i];  
	}  
}
```

#dotnet #csharp #collections 