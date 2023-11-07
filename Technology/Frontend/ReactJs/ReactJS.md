### Concepts

### Why was created

When a web page is load into the browser (html). The browser gets the HTML code and converts it to a tree structure called [[Document Object Model]] (DOM).
React use **components** to create and update DOM. 
A React Application is a tree composed of component with a App component as root.

### Create a React App

**Create React APP - (CRA)**

* ...

**Vite***

* npm create vite@latest

### React project structure

```mermaid 
graph LR; 
id1((src)) --> id2((assets));
id1((src)) --> id3((App.css)); 
id1((src)) --> id4((App.tsx)); 
id1((src)) --> id5((index.css));
id1((src)) --> id6((main.tsx));
id1((src)) --> id7((vite-env.d.ts));
id8((public))
di9((index.html))
id10((package.json))
id11((package-lock.json))
id12((node_modules))
id13((.gitignore))
id14((tscondig.json))
id15((tscondig.node.json))
id16((vite.config.ts))
```


### Create new component

* create new file called `Message.tsx`

```jsx
function Message() {
	return <h1>Hello World</h1>;
}

export default Message;

// usage:
// App.tsx
import Message from './Message';

function App() {
	return <div><Message /></div>
}

export default App;
```

### Check the javascript final code:
* [[babeljs.io]]

### Interpolation

Inside the interpolation symbol `{}` it's possible to add any piece of code that returns a value.

```jsx
function Message() {
	const name = 'Mosh';
	if (name)
		return <h1>Hello {name}</h1>;
	return <h1>Hello World</h1>
}
```

### How React Works

![[Pasted image 20231107170101.png]]

React will renders the Virtual DOM with changes in h1 element. Then will compare with actual DOM and then will change only the h1 element in DOM.
**Note**: Technically, the DOM is manipulated by `react-dom`. You can check in the `package.json` file.

Inside `index.html` it's possible to see a reference to `main.tsx` file. There, `ReactDOM.createRoot()` will 
#frontend #reactjs
 