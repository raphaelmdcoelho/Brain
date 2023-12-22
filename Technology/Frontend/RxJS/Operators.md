### Concepts

Operators are **functions**. There are two kinds of operators:

**Pipeable Operators** are the kind that can be piped to Observables using the syntax `observableInstance.pipe(operator)` or, more commonly, `observableInstance.pipe(operatorFactory())`. Operator factory functions include, `filter(...)`, and `mergeMap(...)`.

When Pipeable Operators are called, they do not _change_ the existing Observable instance. Instead, they return a _new_ Observable, whose subscription logic is based on the first Observable.

**Creation Operators** are the other kind of operator, which can be called as standalone functions to create a new Observable. For example: `[of](https://rxjs.dev/api/index/function/of)(1, 2, 3)` creates an observable that will emit 1, 2, and 3, one right after another. Creation operators will be discussed in more detail in a later section.

**Creation**

* [[Operator - ajax]]
* [[Operator - from]]
* [[Operator - fromEvent]]
* [[Operator - interval]]
* [[Operator - of]]
* [[Operator - range]]
* [[Operator - timer]]
* [[Operator - iif]]

**Join Creation**

* [[Operator - concat]]
* [[Operator - forkJoin]]
* [[Operator - merge]]
* [[Operator - partition]]
* [[Operator - race]]
* [[Operator - zip]]

**Transformation**

* [[Operator - concatMap]]
* [[Operator - groupBy]]
* [[Operator - map]]
* [[Operator - scan]]

**Filtering**

* [[Operator - filter]]
* [[Operator - debounce]]
* [[Operator - debounceTime]]
* [[Operator - distinct]]
* [[Operator - elementAt]]
* [[Operator - first]]
* [[Operator - single]]
* [[Operator - last]]
* [[Operator - skip]]
* [[Operator - take]]
* [[Operator - throttle]]

**Join**

**Multicasting**

**Error Handling**

**Utility**

**Conditional and Boolean**

* [[Operator - every]]

**Mathematical and Aggregate**

* [[Operator - count]]
* [[Operator - max]]
* [[Operator - min]]
* [[Operator - reduce]]

**Custom**

#frontend #rxjs 