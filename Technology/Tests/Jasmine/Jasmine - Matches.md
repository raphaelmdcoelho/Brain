### Concept

Each matcher implements a boolean comparison between the actual value and the expected value. It i responsible for reporting to Jasmine if the expectation is `true` or `false`. Jasmine will then pass or fail the spec.

### Matchers

#### Members

* **not**

It's a `member` that inverts the matcher following this `expect`.

```javascript
expect(something).not.toBe(true);
```

#### Methods

* **nothing**

`expect` nothing explicitly.

```javascript
expect().nothing();
```

* **toBe(expected)**

`expect` the actual value to be `===` to the expected value.

```javascript
expect(thing).toBe(realThing);
```

* **toEqual(expected)**

[`expect`](https://jasmine.github.io/api/edge/global.html#expect) the actual value to be equal to the expected, using deep equality comparison.

```javascript
expect(bigObject).toEqual({"foo": ['bar', 'baz']});
```

* **toBeCloseTo(expected, precision)**

`expect` the actual value to be withing a specified precision of the expected value.

```javascript
expected(number).toBeCloseTo(42.2, 3);
```


* **toBeDefined()**

`expect` the actual value to be defined. (Not `undefined`)

```javascript
expect(result).toBeDefined();
```

* **toBeFalse()**

`expect` the actual value to be `false`.

```javascript
expect(result).toBeFalse();
```

* **toBeFalsey()**

`expect` the actual value to be falsy

```javascript
expect(result).toBeFalsy();
```

* **toBeGreaterThan(expected)**

`expect` the actual value to be greater than the expected value.

```javascript
expect(result).toBeGreaterThan(3);
```

* **toBeGreaterThanOr**Equal(expected)

`expect` the actual value to be greater than or equal to the expected value.

```javascript
expect(result).toBeGreaterThanOrEqual(25);
```

* **toBeInstanceOf(expected)**

`expect`the actual to be an instance of the expected class

```javascript
expect('foo').toBeInstanceOf(string);
expect(3).toBeInstanceOF(Number);
expect(new Error()).toBeInstanceOf(Error);
```

* **toBeLessThan(expected)**

`expect` the actual value to be less than the expected value.

```javascript
expect(result).toBeLessThan(0);
```

* **toBeLessThanOrEqual(expected)**

`expect` the actual value to be less than or equal to the expected value.

```javascript
expect(result).toBeLessThanOrEqual(123);
```

* **toBeNaN()**

`expect` the actual value to be `NaN`.

```javascript
expect(thing).toBeNaN();
```

* **toBeNull()**

`expect`the actual value to be `null`.

```javascript
expect(result).toBeNull();
```

* **toBeTrue()**

[`expect`](https://jasmine.github.io/api/edge/global.html#expect) the actual value to be `true`.

```javascript
expect(result).toBeTrue();
```

* **toBeTruthy()**

[`expect`](https://jasmine.github.io/api/edge/global.html#expect) the actual value to be truthy.

```javascript
expect(thing).toBeTruthy();
```

* **toBeUndefined()**

[`expect`](https://jasmine.github.io/api/edge/global.html#expect) the actual value to be `undefined`.

```javascript
expect(result).toBeUndefined();
```

* **toContain(expected)**

[`expect`](https://jasmine.github.io/api/edge/global.html#expect) the actual value to contain a specific value.

```javascript
expect(array).toContain(anElement); 
expect(string).toContain(substring);
```

<hr>

* **toHaveBeenCalled()**

[`expect`](https://jasmine.github.io/api/edge/global.html#expect) the actual (a [`Spy`](https://jasmine.github.io/api/edge/Spy.html)) to have been called.

* **toHaveBeenCalledBefore(expected)**

[`expect`](https://jasmine.github.io/api/edge/global.html#expect) the actual value (a [`Spy`](https://jasmine.github.io/api/edge/Spy.html)) to have been called before another [`Spy`](https://jasmine.github.io/api/edge/Spy.html).

```javascript
expect(mySpy).toHaveBeenCalledBefore(otherSpy);
```


#Javascript #test #jasmine