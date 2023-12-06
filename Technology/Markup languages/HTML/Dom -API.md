```javascript
let div = document.createElement('div');

div.setAttribute('class', 'blue');

div.textContent = 'Blue';

// not secure:
div.innerHTML = '<span></span>';
```

```javascript
const template = document.createElement('template');

template.innerHTML = `div class="blue">Blue!</div>`;

template.content.cloneNode(true);
```

**note**: The `<template>` HTML element is a mechanism for holding HTML that is not to be rendered immediately when a page is loaded but my be instantiated subsequently during runtime using JavasScript.

Use of `Proxy`:

```javascript
const dom = html`<div>Hello ${ name }!</div>`
```

#markup #html