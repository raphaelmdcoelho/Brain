### Concept

`RxJS` is a library for composing asynchronous and event-based programs by using observables sequences. It provides one core type, the `Observable`, satellite types (Observer, Schedulers, Subjects) and operators inspired by Array methods (map, filter, reduce, every, etc) to allow handling asynchronous events as collections.

ReactiveX combines the `Observer pattern` with the `Iterator pattern` and `functional programming with collections` to fill the need for an ideal way of managing sequences of events.

The essential concepts in RxJS which solve async event management are:

* **Observable**: represents the idea of an ==invokable collection== of ==future values or events==.
* **Observer**: is a collection of callbacks that knows how to listen to values delivered by the Observable.

```typescript
import { Component, OnInit } from '@angular/core';  
import { Observable, of } from 'rxjs';  
  
@Component({  
selector: 'app-example',  
templateUrl: './example.component.html',  
styleUrls: ['./example.component.css']  
})  
export class ExampleComponent implements OnInit {  
	data$: Observable<number>;  
  
	ngOnInit() {  
		this.data$ = of(1, 2, 3, 4, 5);  
	}  
}
```

In this example, `data$` is an Observable that emits the numbers 1 through 5. The `$` at the end of `data$` is a convention that indicates it's an Observable.

You could then use the async pipe (`| async`) in your Angular template to subscribe to this Observable and update your view whenever new data is emitted.

```typescript
<div *ngFor="let number of data$ | async">  
	{{ number }}  
</div>
```

### Types

* [[Observable]]

* [[Satellite]]

* [[Operators]]

#frontend #rxjs