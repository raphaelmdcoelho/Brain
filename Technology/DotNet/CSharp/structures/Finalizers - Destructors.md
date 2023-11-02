### Concepts

Finalizers (historically referred to as destructors) are used to perform any necessary final clean-up when a class instance is being collected by the garbage collector. In most cases, you can avoid writing a finalizer by using the System.Runtime.InteropServices.SafeHandle or derived classes to wrap any unmanaged handle.

The finalizer implicitly calls `Finalize` on the base class of the object. Therefore, a call to a finalizer is implicitly translated to the following code:

```cshap
protected override void Finalize()
{
	try
	{
		// cleanup statments...
	}
	finally
	{
		base.Finalize();
	}
}
```
### Usage

```csharp
class Car
{
	~Car() // finalizer
	{
		// cleanup statements...
	}
}
```

#csharp #dotnet