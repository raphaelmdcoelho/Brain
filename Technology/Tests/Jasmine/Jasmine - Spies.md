
Jasmine has test double functions called `spies`. A spy can stub any function and tracks calls to it and all arguments. A spy only exists in the `describe` or `it` block in which it is defined, and will be removed after each spec. There are special matchers for interacting with spies.

```javascript
spyOn(object, 'method');
```

You can define what the spy will do when invoked with `and`.

```javascript
spyOn(someObj, 'func').and.returnValue(42);
```

You can define also the arguments for the spy to be invoked.

```javascript
spyOn(someObj, 'func').withArgs(1, 2, 3).and.returnValue(42); 
someObj.func(1, 2, 3); // returns 42
```

Properties are more complicated than functions. In Jasmine, you can do anything with a property spy that you can do with a function spy, but you may need to use different syntax. Use `spyOnProperty` to create either a getter or setter spy.

```javascript
it('method', () => {
	spyOnProperty(someObject, "myValue", "get").and.returnValue(30);
	spyOnProperty(someObject, "myValue", "set").and.callThrough();
});
```

Changing the value of an existing spy is more difficult than with a function, because you cannot _refer_ to a property without calling its `getter` method. To get around this, you can save a reference to the spy for later changes.

```javascript
beforeEach(function() {
  this.propertySpy = spyOnProperty(someObject, "myValue", "get").and.returnValue(1);
});

it("lets you change the spy strategy later", function() {
  this.propertySpy.and.returnValue(3);
  expect(someObject.myValue).toEqual(3);
});
```

#Javascript #test #jasmine