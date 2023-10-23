
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

#csharp