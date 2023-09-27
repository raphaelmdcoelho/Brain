## Doc
- https://bun.sh/docs/runtime/nodejs-apis

#### Bun APIs

- [[Server]]
* [[File IO API]]
* [[SQLite API]]

## Package

- Add a package
```
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
```
FOO=hello Bun run dev
```
#### Programatically
```
process.env.FOO = "hello";
```
- dotenv is no longer needed anymore,because Bun reads .env automatically.

#### Read environment variables 
- process.env.VAR
- Bun.env.VAR