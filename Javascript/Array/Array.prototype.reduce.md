The reduce() method of Array instances executes a user-supplied "reducer" callback function on each element of the array. The final result of running the reducer across all elements of the array is a single value.

#### Examples

```
[].reduce((a, v , i) => 
   (
   {...a, [columns[i]: v]}
   ), {}
})
```

#javascript 