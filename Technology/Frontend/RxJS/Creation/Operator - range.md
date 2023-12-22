![[Pasted image 20231221232546.png]]

```javascript
import { range } from 'rxjs';

const numbers = range(1, 3);

numbers.subscribe({
  next: value => console.log(value),
  complete: () => console.log('Complete!')
});

// Logs:
// 1
// 2
// 3
// 'Complete!'
```

#frontend #rxjs 