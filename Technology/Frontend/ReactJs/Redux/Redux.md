### Concepts

Single source of true for all the data in the javascript application.

Modern web applications are represented as a complex tree of components. Components that constantly produce and share data called state. So redux relies on a single *immutable object* that stores all the app state.

**Overview**

1. **Central Store**: Redux maintains the application's state in a single, central store. This store is like a container holding the state of you entire application.
2. **Actions**: Actions are JavaScript objects that describe what happend. For example, an action might be 'user logged in' or 'item added to cart'. They are the only way to send data from your application to the Redux store.
3. **Reducers**: Reducers are pure functions that take the current state and an action as arguments, and return a new state. They specify how the state changes in response to an action sent to the store.
4. **[[Dispatching Actions]]**: To change the state in the Redux store, you dispatch an action. The store runs its reducer function with the current state and the dispatched action, resulting in a new state.
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