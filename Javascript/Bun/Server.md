* Create a server

```
const server = Bun.server({
	port: 3000,
	fetch(req) {
		return new Response("Bun!");
	}
});

console.log(`{server.port}`);
```
