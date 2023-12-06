### Installation

```bash
npm install --save-dev jest
- run test
- npm install @types # to provide autocomplete on vscode
```
**Note**: The ==test files== should be ended with `.test js`.
### Structure

- describe(() => {}): the thing I’m testing (define a test suit)  
- test/it(() => {}): individual test    
- expect(): expectation.  

- [[Jest - Matchers]]
- [[Jest - Globals]]
- [[Jest - Mock Functions]]
### Helper functions for setup and teardown

- beforeEach(() => {})
- Using jest is possible to use the it.todo structure, to make the test pass without implement it, yet.  

### Others
- Cypress is a good tool to run E2E tests.

#Javascript #test #jest