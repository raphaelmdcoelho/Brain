### Concepts

Run a container from a image.

```bash
docker run nginx
```
### Entrypoint

```bash
docker run --entrypoint /bin/bash image-name

docker run -it -v D:\Temp:/app --entrypoint /bin/bash docker-volume
```

### Volume

```bash
docker run -v D:\Local:/REMOTE image
```

#docker #container 