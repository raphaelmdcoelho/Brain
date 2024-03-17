Components are the main building blocks for Angular applications. Each component consist of:

* An HTML template that declares what renders on the page.
* A TypeScript class that defines behaviour.
* A CSS selector that defines how the component is used in a template
* Optionally, CSS styles applied to the template.

By default, a component's styles only affect elements defined in that component's template

### Creating a component

```bash
ng generate component <component-name>
```

### Basic component structure

```typescript
import { Component } from '@angular/core';
```

```typescript
@Component({ // component decorator
	selector: 'app-component-overview',
	templateUrl: './component-overview.component.html',
	styleUrls: ['./component-overview.component.css']
})
```

```typescript
export class ComponentOverviewComponent {

}
```

Every component requires a [[CSS selector]]. A selector instructs Angular to instantiate this component wherever it finds the corresponding tag in template HTML.

#frontend #angular #component
