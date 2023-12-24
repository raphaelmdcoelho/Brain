### Imperative

* How to do.
* Statments.
* Creating statements that tell the computer how to do its thing.

```javascript
const changeBGColor = () => state.backGround = 'black';
```

```javascript
const addTurtle = turtle => turtles.push(turtle);
```

* Imperative code directly accesses the state and changes it.

* The challenge of state management in imperative code is that with growing complexity you may have many parts of the code touching the same state and when your system starts having trouble it may be quite difficult to debug.

```javascript
const myTurtles = ['Snapping Turtle', 'Sulcata Tortoise']; 
const getTortoises = function () {
	let tortoises = [];
	for(let i = 0; i < myTurtles.length; i++) {    
		if(myTurtles[i].toLowerCase().includes('tortoise')) { 
			tortoises.push(myTurtles[i]); 
		} 
	} 
return tortoises; } getTortoises(); // => ['Sulcata Tortoise']
```
### Declarative

* What to do.
* Expressions.
* Expressions focus on provide output relying in the input . Such expression is called `pure function`.
* In declarative programming, changing the external state or causing external actions such as console log, is called `side effect`.
* And changing a value of anything is called `mutation`.
* Working with expressions that map inputs into outputs.

```javascript
const changeBGColor = state => ({...state, background: 'black'});
```

```javascript
const addTurtle = turtles => turtle => [...turtles, turtle];

let addNewTurtle = addTurtle(myTurtles); 
myTurtles = addNewTurtle('turtle3');
```

* Declarative expressions never change the external state.

* In declarative code, you focus on building a `function composition` that takes a number of small functions and strings them together so one function sequentially passes its output as an input to the next function in line. That has many advantages.

```javascript
const myTurtles = ['Snapping Turtle', 'Sulcata Tortoise']; 
const isTortoise = input => input.toLowerCase().includes('tortoise'); 
const getTortoises = input => input.filter(isTortoise); getTortoises(myTurtle); 
// => ['Sulcata Tortoise']

const getDrink = function(age) {
	if(age > 21) {
	 return 'beer'; 
	} else {
	 return 'water';
	} 
} 

const getDrinkTernary = age => age > 21 ? 'beer' : 'water'; 
getDrink(30) === getDrinkTernary(30);
```

<hr>

**Note**:

In functional programming, **functions are first-class citizens**, meaning that they are used as values.

```javascript
const myFunction = function(event) { event.preventDefault(); }; // function is stored in the variable myFunction 
document.getElementById('#turtleLink').addEventListener('click', myFunction); // myFunction is used as an argument for addEventListener function
```

JavaScript also has support for currying, point-free code, partial application, and higher-order functions.