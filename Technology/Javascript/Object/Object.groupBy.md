### Concept

It's used to group element from a given collection.

### Usage

```javascript
let ppl = [
	{ name: "John", age: 2 },
	{ name: "Jane", age: 19 },
	{ name: "Jeff", age: 69 },
];

function adultsOnly({ age }) {
	if(age >= 21) {
		return 'adult';
	else
		return 'minor';
}

const organized = Object.Gropby(ppl, adultsOnly);

// result:
//{ minor: Array(2), adult: Array(1) }
//adult: Array(1)
//	0: { name: 'Jeff', age: 69 }
//	lenght: 1
//	...
```

#javascript 