Single source of true for all the data in the javascript application.

Modern web applications are represented as a complex tree of components. Components that constantly produce and share data called state. So redux relies on a single *immutable object* that stores all the app state.

### Usage

1. install `npm install @reduxjs/toolkit react-redux`.

2. Inside `store.js` file, setup the global store object.

```typescript
import { configureStore } from '@reduxjs/toolkit';
import pizzaReducer from './pizzaSlice';

export const store = configureStore({
	reducer: {
		pizza: pizzaReducer,
	},
});
```

```jsx
...
<React.StrictMode>
	<Provider store={store}>
		<App />
	</Provider>
</React.StrictMode>
```

```typescript
import { createSlice } from '@reduxjs/tookit'

const initialState = {
	toppings: ['pepperoni'],
	gluten: true
}

export const pizzaSlice = createSlice({
	name: 'pizza',
	initialState,
	reducers: {
		tootleGluten: (state) => {
			state.gluten = !state.gluten
		},
		addTopping: (state, action) => {
			state.toppings = [...state.toppings, action.payload]
		}
	}
})

export default { tootleGluten, addTopping } = pizzaSlice.Actions

export default pizzaSlice.reducer
```

#frontend #reactjs 