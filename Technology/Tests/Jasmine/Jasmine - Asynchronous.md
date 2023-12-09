Jasmine supports three ways of managing asynchronous work: `async/await`, promises, and callbacks. If Jasmine doesn't detect one of these, it will assume that the work is synchronous and move on to the next thing in the queue as soon as the function returns. All of these mechanisms work for `beforeEach`, `afterEach`, `beforeAll`, `afterAll` and `it`.

### async / await

Usually, the most convenient way to write async tests is to use `async/await`. `async` functions implicitly return a promise. Jasmine will wait until the returned promise either resolved or rejected before moving on to the next thing in the queue. Rejected promises will cause a spec failure, or a suite-level failure in the case of `beforeAll` or `afterAll`.

```javascript
beforeEach(async function() {
  await someLongSetupFunction();
});

it('does a thing', async function() {
  const result = await someAsyncFunction();
  expect(result).toEqual(someExpectedValue);
});
```

### Failing with `async/await`

`async/await` functions can indicate failure by either returning a rejected promise or by throwing an error.

```javascript
beforeEach(async function() {
  // Will fail if the promise returned by
  // someAsyncFunction is rejected.
  await someAsyncFunction();
});

it('does a thing', async function() {
  // Will fail if doSomethingThatMightThrow throws.
  doSomethingThatMightThrow();

  // Will fail if the promise returned by
  // asyncFunctionThatMightFail is rejected.
  const value = await asyncFunctionThatMightFail();
  // ...
});
```
### Promises 

If you need more control, you can explicitly return a promise instead. Jasmine considers any object with a `then` method to be a promise, so you can use either the Javascript runtime's built-in `Promise` type or a library.

```javascript
beforeEach(function() {
  return new Promise(function(resolve, reject) {
    // do something asynchronous
    resolve();
  });
});

it('does a thing', function() {
  return someAsyncFunction().then(function (result) {
    expect(result).toEqual(someExpectedValue);
  });
});
```

#Javascript #test #jasmine