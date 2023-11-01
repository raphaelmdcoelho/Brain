### Concepts

**What is a file?**

At its core, a file is a contiguous set of bytes used to store data. This data is organized in a specific format and can be anything as simple as a text file or as complicated as a program executable. In the end, these byte files are then translated into binary 1 and 0 for easier processing by the computer.

Files on most modern files systems are composed of **three main parts**:

1. **Header**: metadata about the contents of the file (file name, size, type and so on).
2. **Data**: contents of the files as written by the creator or editor.
3. **[[End-Of-File]] (EOF)**: special character that indicates the end of the file.

What this data represents depends on the format specification used, which is typically represented by an extension. For example, a file that has an extension of .gif most likely conforms to the *Graphics Interchange Format* specification. There are hundreds, if not thousands, of file extensions out there.

**File Paths**

When you access a file on an operating system, a file path is required. The file path is a string that represents the location of a file. It's broken up into **three major parts**:

1. **Folder Path**: the file folder location on the [[File System]] where subsequent folders are separated by a ==forward slash / (Unix) or backslash \ (Windows)==.
2. **File Name**: the actual name of the file.
3. **Extension**: the end of the file path pre-pended with a period (.) used to indicate the file type.

**Line Endings**

One problem often encountered when working with file data is the representation of a new line or line ending. ==The line ending has its roots from back in the Morse Code era, when a specific pro-sign was used to communicate the end of a transmission or the end of a line.==

Later, this was standardized for teleprinters by both the international Organization for Standardization (ISO) and the American Standards Association (ASA). ASA standard states that line endings should use the sequence of the Carriage Return (CR or \r) and the Line Feed (LF or \n) characters (CR+LF or \r\n). The ISO standard however allowed for either the CR+LF characters or just the LF character.

Windows uses the CR+LF characters to indicate a new line, while Unix and the newer Mac versions use just the LF character.

**[[Character Encodings]]**

**Opening and closing a file in python**

```python
file = open('file.txt')
```

```python
reader = open('file.txt')
try:
	# do something
finally:
	reader.close()
```

```python
with open('file.txt') as reader:
	# do something
```

Most likely, you'll also want to use the second positional argument, `mode`. This argument is a string that contains multiple characters to represent how you want to open the file. The default and most common is `r`, which represents opening the file in read-only mode as text file:

```python
with open('file.txt', 'r') as reader:
	# do something
```

The most commonly used ones are the following:

|Character|Meaning|
|---|---|
|`'r'`|Open for reading (default)|
|`'w'`|Open for writing, truncating (overwriting) the file first|
|`'rb'` or `'wb'`|Open in binary mode (read/write using byte data)|

**File object**

"an object exposing a file-oriented API (with ethods such as `read()` or `write()`) to an underlying resource".

There are three different categories of file objects:

* Text files
* Buffered binary files
* Raw binary files

Each of these file types are defined in the `io` module. Here’s a quick rundown of how everything lines up.

* Text File Types:

With these types of files, `open()` will return a `TextIOWrapper` file object:

```python
file = open('file.txt')
type(file)
# <class '_io.TextIOWrapper'>
```

This is the default file object returned by `open()`.

* Buffered Binary File Types:

A buffered binary file type is used for reading and writing binary files. Here are some examples of how these files are opened:

```python
open('file.txt', 'rb')
open('file.txt', 'wb')
```

With these types of files, `open()` will return either a `BufferedReader` or `BufferedWriter` file object:

```python
file = open('file.txt', 'rb')
type(file)
# <class '_io.BufferedReader'>

file = open('file.txt', 'wb')
type(file)
# <class '_io.BufferedWriter'>
```

* Raw File Types:

A raw file type is: "generally used as a low-level building-block for binary and text streams".

It is therefore not typically used.

Here’s an example of how these files are opened:

With these types of files, `open()` will return a `FileIO` file object:

```python
file = open('file.txt', 'rb', buffering=0)
type(file)
# <class '_io.FIleIO'>
```

**Reading and Writing Opened Files**

| Method | What It Does |
|---|---|
| .read(size=-1)| This reads from the file based on the number of `size` bytes. If no argument is passed or `None` or `-1` is passed, then the entire file is read. |
| .readline(size=-1) | This reads at most `size` number of characters from the line. This continues to the end of the line and then wraps back around. If no argument is passed or `None` or `-1` is passed, then the entire line (or rest of the line) is read. |
| .readline() | This reads the remaining lines from the file object and returns them as a list. |

**Iterating Over Each Line in the File**

| Method | What It Does |
|---|---|
| .write(string) | This writes the string to the file. |
| .writelines(seq) | This writes the sequence to the file. No line endings are appended to each sequence item. It's up to you to add the appropriate line ending(s). |

```python
with open('file.txt', 'r') as reader:
	text = reader.readlines()

with open('reversed.txt', 'w') as writer:
	for line in reversed(text):
		writer.write(line)
```

**Working With Bytes

Sometimes, you may need to work with files using byte strings. This is done by adding the 'b' character to the `mode` argument. All of the same methods for the file object apply. However, each of the methods expect and return a bytes object instead:

```python
with open('file.txt', 'rb') as reader:
	print(reader.readline())
```

Example of a `.png` file structure:

|Value|Interpretation|
|---|---|
|`0x89`|A “magic” number to indicate that this is the start of a `PNG`|
|`0x50 0x4E 0x47`|`PNG` in ASCII|
|`0x0D 0x0A`|A DOS style line ending `\r\n`|
|`0x1A`|A DOS style EOF character|
|`0x0A`|A Unix style line ending `\n`|

```python
with open('image.png', 'rb') as byte_reader:
	print(byte_reader.read(1))
	print(byte_reader.read(3))
	print(byte_reader.read(2))
	print(byte_reader.read(1))
	print(byte_reader.read(1))

# b'\x89'
# b'PNG'
# b'\r\n'
# b'\x1a'
# b'\n'
```

**Dos2Unix.py**

#python 