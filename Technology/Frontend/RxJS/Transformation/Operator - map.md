![[Pasted image 20231221233713.png]]

```javascript
import { of, map } from 'rxjs';

of(1, 2, 3)
  .pipe(map((x) => x * x))
  .subscribe((v) => console.log(`value: ${v}`));

// Logs:
// value: 1
// value: 4
// value: 9
```

```javascript
import { fromEvent, map } from 'rxjs';

const clicks = fromEvent<PointerEvent>(document, 'click');
const positions = clicks.pipe(map(ev => ev.clientX));

positions.subscribe(x => console.log(x));
```

#frontend #rxjs