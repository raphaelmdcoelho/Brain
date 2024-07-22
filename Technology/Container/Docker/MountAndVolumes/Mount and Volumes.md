### Named Volumes ###

```bash
docker volume create my-ts-app-data

docker run -d -p 3000:3000 -e DATABASE_URL=mongodb://mongo:27017/ts-express-app -v my-ts-app-data:/data/db ts-express-app

docker volume rm my-ts-app-data
```

![[Pasted image 20240708232754.png]]
### Bind Mounts ###
### tmpfs Mounts ###

#docker #container 