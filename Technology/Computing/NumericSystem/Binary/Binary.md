### Concepts

* 8 bits is equivalent to 1 byte.
* 1 character has 8 bits.
* 8 bits has a capacity of 256 combinations.
* Range: 0 - 255.
* binary from a character: 0000 0000.
* hexadecimal from it: 00.
* Conversion:
	* Binary to HEX: /4.
	* HEX to binary: *4.
	* Decimal to binary: divides until zero and then concatenates the rest (1 or 0).

### Manipulation

How to see a binary content:

```bash
xxd -b file.txt (binary)
xxd file.txt (hexadecimal)
```

* [[Bitwise Operator]]

#numericsystem