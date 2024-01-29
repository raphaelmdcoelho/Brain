### Concepts

**Class*

```javascript
function Book(tile, pages, isbn) {
	this.tile = title,
	this.pages = pages,
	this.isbn = isbn,
	this.IsOld = function() {
		return !!this.isbn
	}
}

let book = new Book(...);

Book.prototype.printTile = function() {
	console.log('');
}
```

**Note**: Using `prototype` the same property will be shared between all instances, but declaring the method in the class definition, each instance will have its all value for the method.

**Object**

creating a object:

```javascript

let obj = new Object();

let obj = {}

let obj = {
	name: {
		first: '',
		last: ''
	},
	dtBirth: new Date()
}

```
### Classes

- [[Object]]
- [[String]]
- [[Array]]

### Methods

* [[Javascript - eval()]]

### Tests

- [[Jest]]

### Operators

* [[double exclamation mark]]
* [[javascript - spread]]

### Frameworks

* [[Bun]]
* [[Node]]

#javascript 


