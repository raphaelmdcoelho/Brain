### Observable (Publisher)

```typescript
interface Observable {
	subscribe(o: Observer): void;
	unsubscribe(o: Observer): void;
	notify(): void;
}
```

```typescript
class Publisher implements Observer {
	private message: string = "";
	private observers: Array<Observer> = [];

	setMessage(message: string): void {
		this.message = message;
		this.notify();
	}
	
	subscribe(o: Observer): void {
		this.observers.push(o);
	}

	unsubscribe(o: Observer): void {
		const index = this.observers.indexOf(o);
		this.observers.splice(index, 1);
	}

	nofity(): void {
		for(const observer of this.observers) {
			this.observer.update(this.message);
		}
	}
}
```

### Observer (Subscriber)

```typescript
interface Observer {
	update(message: string): void;
}
```

```typescript
class Subscriber implements Observer {
	private observable: Observable;
	
	constructor(observable: Observable) {
		this.observable = observable;
		this.observable.subscribe(this);
	}

	update(message: string): void {
		console.log(`the event ${} happend.`);
	}
}
```

### Running it

```typescript
const publisher = new Publisher();
const subscriber = new Subscriber(publisher);

publisher.setMessage("hello");
publisher.unsubscribe(subscriber);
publisher.setMessage("other message");
```

### References

* https://dev.to/vivekalhat/observer-pattern-for-beginners-5h64

#patterns #computing