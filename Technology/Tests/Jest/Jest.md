- npm install --save-dev jest
- run test
- npm install @types to provide autocomplete on vscode
- The test files should be ended with **.test js**

***Structure***
- describe(() => {}): the thing I’m testing (define a test suit)  
- test/it(() => {}): individual test    
- expect(): expectation.  
- toBe()/toEqual(): Matcher to test the actual value compare to expected.
    
***Helper functions for setup and teardown***
- beforeEach(() => {})
- Using jest is possible to use the it.todo structure, to make the test pass without implement it, yet.  

***Others***
- Cypress is a good tool to run E2E tests.

#Javascript #test