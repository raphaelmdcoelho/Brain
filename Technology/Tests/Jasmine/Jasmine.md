### Installation

```bash
npm install --save-dev jasmine

npm test
```

Set jasmine as your test script in your `package.json`.

```json
"scripts": { "test": "jasmine" }
```


### Structure

```javascript
describe("A suite", function() {
    it("contains spec with an expectation", function() {
        expect(true).toBe(true);
    });
});
```

**Describe** function is for grouping related specs, typically each test file has one at the top level. The string parameter is for naming the collection of specs, and will be concatenated with specs to make a spec's full name.

**Specs** are defined by calling the global Jasmine function `it`, which, like describe, takes a string and a function.

#Javascript #test #jasmine