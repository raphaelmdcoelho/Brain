
### Concepts

You can add an event handler to an element by:

1. Adding an attribute with the events name inside of parentheses
2. Specify what JavaScript statement you want to run when it fires

```typescript
// text-transformer.component.ts
@Component({
  standalone: true,
  selector: 'text-transformer',
  template: `
    <p>{{ announcement }}</p>
    <button (click)="transformText()">Abracadabra!</button>
  `,
})
export class TextTransformer {
  announcement = 'Hello again Angular!';
  transformText() {
    this.announcement = this.announcement.toUpperCase();
  }
}
```

```html
<input (keyup)="validateInput()" />
<input (keydown)="updateInput()" />
```

### $Event

If you need to access the [event]([Event - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Event)) object, Angular provides an implicit `$event` variable that you can be pass to a function:

```html
<button (click)="createUser($event)">Submit</button>
```

#frontend #angular  #event