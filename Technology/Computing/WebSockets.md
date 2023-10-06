### What are WebSockets?

WebSockets provide a ***full-duplex*** communication channel over a single, long-lived connection. Unlike HTTP, which is request-response based, WebSockets enable the server to send data to the client without being prompted by the client, and vice versa. This makes WebSockets very useful for real-time applications.

### How Do WebSockets Work?

1. **Initial Handshake**: First, a regular HTTP connection is established between the client and the server.
2. **Upgrade Request**: The client sends an HTTP "Upgrade" request to switch from HTTP to WebSocket protocol.
3. **Upgrade Response**: The server sends back a confirmation that it supports this protocol, and the WebSocket connection is established.

## Characteristics

* Two way connection between a client and a server.
*  How it occurs:
	* First the client send a request to the server.
```
GET ws://some-url HTTP/1.1
Connection: Upgrade
Upgrade: websocket
```
		* If server agress, it will send a 101 response:
```
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
```
* The the ***handshake*** is complete and the ***TCP/IP*** connection is left open.
* It is a ***Full-duplex*** connection.

## NodeJS example

```javascript
// BACKEND
npm install ws
const server = new WebSocket.Server({ port: '8080'})

server.on('connection', socket => { // the first event to happen is the connection from the client
	socket.on('message', message => {
		socket.send(`Roger that! ${message}`)
	})
})

//FRONTEND
// listen for messages
const socket = new WebSocket('ws://localhost:8080') // ws protocol

socket.onmessage = ({ data }} => {
	CONSOLE.LOG('mESSAGE FROM SERVER ', DATA)
})

document.querySelector('button').onclick = () => {
	socket.send('hello')
}
```

## Bash Example
```bash
curl -i -N  \
    -H "Connection: Upgrade" \
    -H "Upgrade: websocket" \
    -H "Host: echo.websocket.org" \
    -H "Origin:http://www.websocket.org"  \
    http://echo.websocket.org

HTTP/1.1 101 Web Socket Protocol Handshake
Upgrade: WebSocket
Connection: Upgrade
WebSocket-Origin: http://www.websocket.org
WebSocket-Location: ws://echo.websocket.org/
Server: Kaazing Gateway
Date: Mon, 11 Jun 2012 16:34:46 GMT
Access-Control-Allow-Origin: http://www.websocket.org
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: content-type
Access-Control-Allow-Headers: authorization
Access-Control-Allow-Headers: x-websocket-extensions
Access-Control-Allow-Headers: x-websocket-version
Access-Control-Allow-Headers: x-websocket-protocol
```

## Socket.io
```javascript
npm init -y
npm install socket.io
```

```javascript
//BACKEND
const http = require('http').createServer()

const io = require('socket.io')(http, {
	cors: { origin: "**" }
})

io.on('connection', (socket) => {
	console.log('a user connected')
	socket.on('message', (message) => { // use any custom event name here
		console.log(message)
		io.emit('message', `${socket.id.substr(0,2)} said ${message}`)
	}) 
})

http.listen(8080, () => console.log('listening on http://localhost:8080'))

//FRONTEND
//index.html
...
<head>
	<script src="https://cdn.socket.io/socket.io-3.0.0.js"></script>
</head>
...
//app.js
const socket = io('ws://localhost:8080')

socket.on('message', text => {
	const el = document.createElement('li')
	el.innerHTML = text
	document.querySelector('ul').appendChild(el)
})

document.querySelector('button').onclick = () => {
const text = document.querySelector('input').value
socket.emit('message', text)
}
```

#computing 