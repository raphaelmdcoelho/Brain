
### Concepts

`Test doubles` are objects that are used in tests to replace real components, providing controlled behavior and observations necessary for testing.
Its purpose are being used to isolate the component under test, making the tests more reliable and faster. They can also be useful when the real objects are impractical to use in test.

### Types

* **Stubs**: These are the simples kind of test double. Stubs provide canned answers to calls made during the test. ==They are typically used when you need to provide an input to the system under test but don't want to use a real object==.
	* No logic, just return whichever the test do.
* **Mocks**: Mocks are used to verify interactions between objects. In other words, ==they are about behavior rather than state==. They are pre-programmed with ==expectations== and also ==verify that they receive the calls they expect==, often specifying the ==order of calls==.
* **Spies**: Spies are similar to mocks, but they are typically ==used to record information about how they were called==. For example, you might spy on a method to see ==how many times it was called and with what arguments==. They are useful when you want to perform assertions on the interactions with the spy.
* **Fakes**: Fakes are objects that have ==working implementations, but not the same as the production one==. They are usually simpler, taking shortcuts and have limitations compared to the real object.
* **Dummies**: Dummies are the simplest form of test doubles. They are passed around but never actually used. Essentially, they are placeholders. They are used when a parameter is needed for the tested method but without actually needing to use the parameter.

#test