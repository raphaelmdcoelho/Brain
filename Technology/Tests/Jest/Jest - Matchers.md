### Definition

Jest uses `matchers` to let you test values in different ways.

### Structure

***toBe***

```javascript
test('two plus two is four', () => {
	expect(2 + 2).toBe(4);
});
```
**Note**: `toBe` uses `Object.is` to test exact equality.

***toEqual***

If you want to check the value of an object, use `ToEqual`:
```javascript
test('object assignment', () => {  
const data = {one: 1};  
data['two'] = 2;  
expect(data).toEqual({one: 1, two: 2});  
});
```
**Note**: `toEqual` recursively checks every field of an object or array.

***toStrictEqual***

Compares object taking in consideration undefined values. `ToEqual` ignore them.

***not***

```javascript
test('adding positive numbers is not zero', () => {  
	for (let a = 1; a < 10; a++) {  
		for (let b = 1; b < 10; b++) {  
			expect(a + b).not.toBe(0);  
		}  
	}  
});
```

***toBeNull*** 

Matches only `null`.

***toBeUndefined***

Matches only `undefined`.

***toBeDefined***

Is the opposite of `toBeUndefined`.

***toBeTruthy***

Matches anything that an `if` statement treats as true.

***toBeFalsy*** 

Matches anything that an `if` statement treats as false.



#Javascript #test #jest