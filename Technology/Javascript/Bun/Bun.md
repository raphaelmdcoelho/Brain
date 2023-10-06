## Doc
- https://bun.sh/docs/runtime/nodejs-apis

#### Bun APIs

- [[BUN - Server]]
* [[BUN - File IO]]
* [[BUN - SQLite API]]

## Package

- Add a package
```javascript
bun add package
```

## Run

- It's possible to use --watch flag to have watch mode.

## Environment variables

#### Bun reads the following files automatically
	* .env
	* .env.production, .env.development, .env.test (depending on value NODE_ENV)
	* .env.local
.env content:
FOO=hello
#### Variables can also be set via the command line:
```javascript
FOO=hello Bun run dev
```
#### Programatically
```javascript
process.env.FOO = "hello";
```
- dotenv is no longer needed anymore,because Bun reads .env automatically.

#### Read environment variables 
- process.env.VAR
- Bun.env.VAR

#bun #javascript 