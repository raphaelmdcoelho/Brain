The `USER` instruction sets the user name (or UID) and optionally the user group (or GID) to use as the default user and group for the remainder of the current stage. The specified user is used for `RUN` instructions and at runtime, runs the relevant `ENTRYPOINT` and `CMD` commands.

```Dockerfile
USER root
```

```Dockerfile
RUN useradd -ms /bin/bash newuser 
USER newuser

RUN echo "The current user is $(whoami)"
RUN chown myuser:myuser ./entrypoint.sh
RUN chmod +x ./entrypoint.sh
```

#docker #container 
