### Concepts

The `~` operator produces a complement bit by bit of its value inverting each bit:
### Usage

```csharp
uint a = 0b_0000_1111_0000_1111_0000_1111_0000_1100; uint b = ~a; Console.WriteLine(Convert.ToString(b, toBase: 2));
// Output: 
// 11110000111100001111000011110011
```

#dotnet #csharp 