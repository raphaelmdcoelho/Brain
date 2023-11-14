* It runs at each renderization:

```typescript
import { useEffect } from 'react';

function App() {
	useEffect(() [> {
		console.log(count);
	});
}
```

* Will run only when a control value changes:
  
```typescript
useEffect(() [> {
		console.log(count);
	}, [count]);
```

* Will run only when the page is loaded.

```typescript
useEffect(() [> {
		fetch('https://url.com')
			.then(data => console.log(data))
	}, []);
```

* clean up function:

```typescript
useEffect(() => {
	const timer = setTimeout(() => {
		console.log(`message ${count}`)
	}, 2000);

	return () => {
		clearTimeout(timer);
	};
}, [count])
```

#frontend #reactjs #hooks 