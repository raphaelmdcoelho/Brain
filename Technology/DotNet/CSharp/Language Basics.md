`Statements` in C# execute sequentially and are terminated by a semicolon.
A the outermost level, types are organized into `namespaces`.
A `statment block` is a series of statements surrounded by pair of braces.

### Compilation

The C# compiler compiles source code (a set of files with the .cs extension) into an [[Assembly]]. ==An assembly is the unit of packaging and deployment in .NET==. ==An assembly can be either an application or a library==. A normal console or Windows application has an entry point, whereas a library does not. The purpose of a library is to be called upon (referenced) by an application or by other libraries. .NET itself is a set of libraries (as well as a runtime environment).

The [[DotNet Tool]] (dotnet.exe on Windows) helps you to manage .NET source code and binaries from the command line. You can use it to both build and run your program, as an alternative to using an integrated development environment (IDE) such as Visual Studio or Visual Studio Code.

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
* async
* await
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



#csharp #dotnet 