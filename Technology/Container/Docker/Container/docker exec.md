### Concepts

The docker exec command allows you to run commands inside a running Docker container.

### Commands

```bash
docker exec -it [container-id] /bin/bash

docker exec [OPTIONS] CONTAINER_ID|CONTAINER_NAME COMMAND [ARG…]
```

- OPTIONS: Various options like `-it` for interactive mode.
- CONTAINER: The name or ID of the container.
- COMMAND: The command you want to run inside the container.
- ARG: Arguments for the command.

#docker #container 