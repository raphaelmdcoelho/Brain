`Statements` in C# execute sequentially and are terminated by a semicolon.
A the outermost level, types are organized into `namespaces`.
A `statment block` is a series of statements surrounded by pair of braces.

### Compilation

The C# compiler compiles source code (a set of files with the .cs extension) into an `Assembly`. ==An assembly is the unit of packaging and deployment in .NET==. ==An assembly can be either an application or a library==. A normal console or Windows application has an entry point, whereas a library does not. The purpose of a library is to be called upon (referenced) by an application or by other libraries. .NET itself is a set of libraries (as well as a runtime environment).

The `DotNet Tool` (dotnet.exe on Windows) helps you to manage .NET source code and binaries from the command line. You can use it to both build and run your program, as an alternative to using an integrated development environment (IDE) such as Visual Studio or Visual Studio Code.

### Syntax

C# syntax is inspired by C and C++ syntax. In this section, we describe C#'s elements of syntax, using the following program:

```csharp
using System;

int x = 12 * 30;
Console.WriteLine(x);
```

**Identifiers and Keywords**

Identifiers are names that programmers choose for their classes, methods, variables, and so on. Here are the identifiers in our example program, in the order in which they appear:

`System x Console WriteLine`

An identifier must be a whole word, essentially made up of Unicode characters starting with a letter or underscore. C# identifiers are case sensitive. By convention, parameters, local variables, and private fields should be in camel case, and all other identifiers should be in Pascal case.

==Keywords are names that mean something special to the compiler==. There are two keywords in our example program, using and int.

Full list of keywords reserveds:

* abstract
* as
* base
* bool
* break
* byte
* case
* catch
* do
* double
* else
* enum
* event
* explicit
* extern
* false
* in
* int
* interface
* internal
* is
* lock
* long
* namespace
* protected
* public
* readonly
* record
* ref
* return
* sbyte
* sealed
* throw
* true
* try
* typeof
* uint
* ulong
* unchecked
* unsafe
* char
* checked
* class
* const
* continue
* decimal
* default
* delegate
* fially
* fixed
* float
* for
* foreach
* goto
* if
* implicit
* new
* null
* object
* oerator
* out
* override
* params
* private
* short
* sizeof
* stackalloc
* static
* string
* struct
* switch
* this
* ushort
* using
* virtual
* void
* volatile
* while

if you really want to use an identifier that clashes with a reserved keyword, you can do so by qualifying it with the @ prefix; for instance:

```csharp
int using = 123; // Illegal
int @using = 123; // Legal
```

**Contextual keywords**

Some keywords are contextual, meaning that you also can use them as identifiers - without an @ symbol:

* add
* alias
* and
* ascending
* async - await
* by
* descending
* dynamic
* equals
* from
* get
* global
* group
* init
* into
* join
* let
* managed
* nameof
* nint
* not
* notnull
* nuint
* on
* or
* orderby
* partial
* remove
* select
* set
* unmanaged
* value
* var
* with
* when
* where
* yield

**Literals, Punctuators and Operators

* Literals are primitive pieces of data lexically embedded into the program.
* Punctuators help demarcate the structure of the program (semicolon).
* An Operator transforms and combines expressions.

### Type Basics

A type defines the blueprint for a value. 

A variable denotes a storage location that can contain different values over time. In contrast, a constant stores always represent the same value.

In C#, predefined types (also referred to as built-in types) are recognized with a C# keyword.

**Members of a type**

A type contains `data members` and `function members`. The data member can also be called `field`.

**Instance vs static members**

The data members and function members that operate on the instance of the type are called instance members.

**public keyword**

The public keyword exposes members to other classes. 

**Defining a Main method**

Without Top-level statements a simple console or Windows application looks like this:

```csharp
using System;

class Program
{
	static void Main()
	{
		int x = 12 * 30;
		Console.WriteLine(x);
	}
}

class Program
{
	static int Main(string[] args)
	{
		...
	}
}
```

The Main method can also be declared async and return `Task` or `Task<int>`` in support of asynchronous programming.

**Top-Level Statements**

Top-level statements (introduced in C# 9)  let you avoid the baggage of a static Main method and a containing class. A file with top-level statements comprises three parts, in this order:

1. (Optionally) using directives.
2. A series of statements, optionally mixed with method declarations.
3. (Optionally) Type and namespace declarations.

Top-level statements can access a "magic" variable of type string[] called `args`, corresponding to command-line arguments passed by the caller.

### Type and Conversions

C# can convert between instances of compatible types. A conversion ==always creates a new value from an existing one==. Conversions can be either `implicit` or `explicit`: implicit conversions happen automatically, and explicit conversions require a `cast`. In the following example, we implicitly convert an int to a long type( which has twice the bit capacity of an int) and explicitly cast an int to a short type (which has half the bit capacity of an int):

```csharp
int x = 12345; // int is a 32-bit integer
long y = x; // Implicit conversion to 64-bit integer

short z = (short)x; //  Explicity conversion to 16-bit integer
```

Implicit conversions are allowed when both of the following are true:

* The compiler can guarantee that they will always succeed.
* No information is lost in conversion.

Conversely, explicit conversions are required when one of the following is true:

* The compiler cannot guarantee that they will always succeed.
* Information might be lost during conversion.

The numeric conversions that we just saw are built into the language. C# also supports reference conversions and ==Boxing Conversions== as well as custom conversions. The compiler doesn't enforce the aforementioned rules with custom conversions, so it's possible for badly designed types to behave otherwise.

### Value Types Versus Reference Types

All C# types fall into the following categories:

* [[Value types]]
* [[Reference types]]
* [[Generic type parameters]]
* [[Pointer types]]
### Storage overhead

Value-type instances occupy precisely the memory required to store their fields. In this example, Point takes 8 bytes of memory:

```csharp
struct Point
{
	int x; // 4 bytes
	int y; // 4 bytes
}
```

Reference types require separate allocations of memory for the reference and object. The object consumes as many bytes as its fields, plus additional administrative overhead. The precise overhead is intrinsically private to the implementation of the .NET runtime, but at minimum, the overhead is 8 bytes, used to store a key to the object's type as well as temporary information such as its lock state of multithreading and a flag to indicate whether it has been fixed from movement by the garbage collector. ==Each reference to an object requires an extra 4 or 8 bytes==, depending on whether the .NET runtime is running on a 32-bit or 64-bit platform.
### Predefined Type Taxonomy

The predefined types in C# are as follows:

* Value types
	**Numeric**
		- Signed integer (sbyte, short, int long)
		- Unsigned integer (byte, ushort, uint, ulong)
		- Real number (float, double, decimal)
	**Logical (bool)**
	**Character (char)
* Reference types
	**String (string)**
	**Object(object)**

Predefined types in C# alias .NET types in the System namespace. There is only a syntactic different between these two statements:

```csharp
int i = 5;
System.Int32 i = 5;
```

The set of predefined value types excluding `decimal` are known as `primitive types` in the `CLR`. Primitive types are so called because they are supported directly via instructions in compiled code, and this usually translates to direct support on the underlying processor; for example:

```csharp
// Underlying hexadecimal representation

int i = 7; // 0x7
bool b = tue; // 0x1
char c = 'A'; // 0x41
float f = 0.5f; // uses IEEE floating-point encoding
```

The ==System.IntPtr== and ==System.UIntPtr== types are also primitive.

### Numeric Types

C# has the predefined numeric types shown as:

| **C# type** | **System type** | **Suffix** | **Size** | **Range** |
|---|---|---|---|---|
| Integral-signed | | | |  |
| sbyte | SByte| | 8-bits | -2<sup>7</sup> to 2<sup>7</sup>-1 |
| short | Int16 | | 16-bits | -2<sup>15</sup> to 2<sup>15</sup>-1 |
| int | Int32 | | 32-bits | -2<sup>31</sup> to 2<sup>31</sup>-1 |
| long | Int64 | | 64-bits | -2<sup>63</sup> to 2<sup>63</sup>-1 |
| nint | IntPtr | | 32/64 bits | |
| Integral-unsigned | | | | |
| byte | Byte | | 8-bits | 0 to 2<sup>8</sup>-1 |
| ushort | UInt16 | | 16-bits | 0 to 2<sup>16</sup>-1 |
| uint | UInt16 | U | 16-bis | 0 to 2<sup>16</sup>-1 |
| ulong | UInt64 | UL | 64-bits | 0 to 2<sup>64</sup>-1 |
| unint | UIntPtr | | 32/64-bits | |
| Real | | | | |
| float | Single | F |32-bits | +-(~10<sup>-45</sup> to 10<sup>38</sup>) |
| double | Double | D | 64-bits | +-(~10<sup>-324</sup> to 10<sup>308</sup>) |
| decimal | Decimal | M | 128-bits | +-(~10<sup>-28</sup> to 10<sup>28</sup>) |

### Numeric Literals

`Integral-type literals` can use decimal or hexadecimal notation; ==hexadecimal is denoted with the 0x prefix==.

```csharp
iny x = 123;
long y = 0x7F;
```

You can insert an underscore anywhere within a numeric literal to make it more readable:

```csharp
int million = 1_000_000;
```

You can specify numbers in binary with the 0b prefix:

```
var b = 0b1010_1011_110_1110_1111;
```

`Real literals` can use decimal and/or exponential notation:

```csharp
double d = 1.5;
double million = 1E06;
```

### Numeric literal type inference

By default, the compiler infers a numeric literal to be either double or an integral type:

* If the literal contains a decimal point or the exponential symbol (E), it is a double.
* Otherwise, the literal's type is the first type in this list that can fit the literal's value: int, uint, long, and ulong.

### Numeric suffixes

Numeric suffixes explicitly define the type of a literal. Suffixes can be either lowercase or uppercase, and are as follows:

* F -> float
* D -> double
* M -> decimal
* U -> uint
* L -> long
* UL -> ulong

### Numeric Conversions

A good class to use when converting numerical classes, are `System.Convert`.

Implicitly converting a large integral type to a floating-point type preserves `magnitude` but can lose `precision`.

!!!!! This happens because floating point types always have more magnitude than integral types but can have less precision.

```csharp
int i1 = 100_000_001;
float f = i1; // magnitude preserved, precision lost
int i2 = (int)f; //100_000_000
```

### Overflow

At runtime, arithmetic operations on integral types can overflow. By default, this happens silently - no exception is throw, and the result exhibits "wraparound" behaviour, as through the computation were done on a larger integer type and the extra significant bits discharged. For example, decrementing a minimum possible for a integer type results in the maximum possible int value:

```csharp
int a = int.MinValue;
a--;
Console.WriteLine(a == int.MaxValue); // True
```

### Overflow check operators

The checked operator instructs the runtime to generate an `OverflowException` rather than overflowing silently.
It's possible to use the checked around either an `expression` or a `statment` block:

```csharp
int a = 1000000;
int b = 1000000;

int c = checked (a * b); // Checks just the expression

checked // Check all expression in statment block
{
	c = a * b;
}
```

It's possible to do that at project level as well.

It's possible to skip the check with the word `unchecked`.

### Bitwise operators

| Operator | Meaning | Sample expression |  Result |
| -- | -- | -- | -- |
| ~ | Complement | ~0xfU | 0xfffffff0U |
| & | And | 0xf0 & 0x33 | 0x30 |
| \| | Or | 0xf0 \| 0x33 | 0xf3 |
| ^ | Exclusive Or | 0xff00 ^ 0x0ff0 | 0xf0f0 |
| << | Shift left | 0x20 << 2 | 0x80 |
| >> | Shift right | 0x20 >> 1 | 0x10 |

**Note**: The `bitwise` operators do the math in binary representation, so in the first example using the `not` operator, 0xfU is representing the decimal 10 without sign. When flipping it value in binary we need to to that for the whole 32 bits (int):

```
! 0000 0000 0000 0000 0000 0000 0000 1111 => 1111 1111 1111 1111 1111 1111 1111 0000
0xfU => 0xfffffff0U
```

**Note**: It's possible to note that doing operations like `and` the smallest hexadecimal will be preserved on the operation result and `zero` values will be preserved also.

### Special float and double values



#csharp #dotnet 