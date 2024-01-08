
### If

```html
@if (isAdmin) {
	<button>Erase database</button>
} @else {
	<p>You are not authorized.</p>
}
```

### For

```html
@for (ingredient of ingredientList; track ingredient.name) {
	<li>{{ ingredient.quantity }} - {{ ingredient.name }}</li>
}
```

**Track**:  When Angular renders a list of elements with `@for`, those items can later change or move. Angular needs to track each element through any reordering, usually by treating a property of the item as a unique identifier or key.

#frontend #angular #directives