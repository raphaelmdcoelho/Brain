## Delegate
```csharp
// DELEGATE

public class Test
{
		public delegate void Print(string message);

		public void PrintHandler(string message)
		{
				Console.WriteLine(message);
		}

		public void Run(Print handler)
		{
				handler.Invoke();
		}

		Run(PrintHandler(string message);
}
```