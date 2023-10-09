## C# 8:

### Indices and ranges

* Indices and ranges simplify working with elements or portions of an array.
* Indices let you refer to elements relative to the end of an array by using the ^ operator. ^1 refers to the last element, ^2 refers to the second-to-last element, and so on.

```csharp
char[] vowels = new char[] {'a','e','i','o','u'}; 
char lastElement = vowels [^1]; // 'u'
char secondToLast = vowels [^2]; // 'o'
```

- Ranges let you “slice” an array by using the `..` operator:

```csharp
char[] firstTwo = vowels [..2];
char[] lastThree = vowels [2..];
char[] middleOne = vowels [2..3];
char[] lastTwo = vowels [^2..];
```

* C# has types Index and Range

```csharp
Index last = ^1; Range firstTwoRange = 0..2; char[] firstTwo = vowels [firstTwoRange]; // 'a', 'e'
```

* You can support indices and ranges in your own classes by defining an indexer with a parameter type of Index or Range:

```csharp
class Sentence {  string[] words = "The quick brown fox".Split();   public string this [Index index] => words [index];  public string[] this [Range range] => words [range]; }
```



#csharp