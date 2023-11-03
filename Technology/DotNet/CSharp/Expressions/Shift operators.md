### Concepts

**Shift left operator** (multiplication)

The `<<` operator moves  the entire value to the left, vanishing the most left bit value and adding one bit to the most right position.

```csharp
uint x = 0b_1100_1001_0000_0000_0000_0000_0001_0001; Console.WriteLine($"Before: {Convert.ToString(x, toBase: 2)}"); 
uint y = x << 4; 
Console.WriteLine($"After: {Convert.ToString(y, toBase: 2)}"); 
// Output: 
// Before: 11001001000000000000000000010001 
// After: 10010000000000000000000100010000
```

**Shift right operator** (division)

```csharp
uint x = 0b_1001; Console.WriteLine($"Before: {Convert.ToString(x, toBase: 2), 4}"); uint y = x >> 2;
Console.WriteLine($"After: {Convert.ToString(y, toBase: 2).PadLeft(4, '0'), 4}"); 
// Output: 
// Before: 1001 
// After: 0010
```


#dotnet #csharp 