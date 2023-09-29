A code smell to check if we need to apply this patern is when we have a lot of parameters within a constructor.

We have a client that injects a Director that receives a interface of builder. For that Builder interface we can create a ConcreteBuilder that will have all the steps to create a product that is also a dependency for it.

![[Pasted image 20230928230700.png]]
#patterns