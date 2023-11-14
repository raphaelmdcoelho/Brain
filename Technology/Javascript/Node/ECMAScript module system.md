### Import default

There is only one by module, and don't need curly braces and the name to be imported can be anyone:

```typescript
import AB from './A'

export default {}
```

### Named Import

It's possible to have many named imports and the name should be exactly the same in the module.

```typescript
import { A, B } from './A'

export const A;
export const B;
```

#node #javascript 