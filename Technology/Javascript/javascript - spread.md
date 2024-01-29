
```javascript
//ES2015
let params = [1,2,3];
sum(...params);

//ES5
sum.apply(undefined, params);
```

```javascript
function count(...a) {
 return a.length
}

count(1,2,3,4,5);
```

```javascript
let array1 = [1,2,3,4]

let array2 = [5, ...array1];
```

#javascript