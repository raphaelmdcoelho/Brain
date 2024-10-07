
It is the process in which interpreter moves the declarations of variables, functions, classes and imports to the top of their scope before the execution of code.

**In na nutshell, hoisting comes from theinterpreter splitting variable declaration and assignment**

Whenever a JavaScript code executed, it runs in the "Execution context" in two phase.

1. Memory Phase (Creation Phase).
2. Code Execution Phase.

## Memory Phase

**Function Declarations**: The entire function is stored in memory, making it available to be called even before the line of code appears.

**Variables with `var`**: Variables declared with var are assigned a default value of undefined. The variable is hoisted, but it won't hold its actual value until the Execution Phase.

**Variables with `let` and `const`**: These are also hoisted but remain uninitialized (in a "temporal dead zone"). They cannot be accessed before their declaration, leading to a `ReferenceError` if you try.

**`Class` Declarations**: Classes are hoisted, but like let and const, remain in the "temporal dead zone" until their declaration is reached. Accessing them earlier will throw a `ReferenceError`.

**`Arrow` Functions**: These are treated like variables and not hoisted as regular functions. They behave like variables declared with const.

## Code Execution Phase

**For `Function` Declarations**: Since functions are fully hoisted during the memory phase, you can call them anytime in the code, even before their declaration.

**For Variables (`var, let, const`)**: Variables declared with var will now be assigned their values. However, let and const only get initialized in this phase, and accessing them before initialization will still result in errors.

**For Classes**: Similarly, classes only get initialized here and trying to instantiate them before this phase will throw an error.

#technology #computing #javascript 