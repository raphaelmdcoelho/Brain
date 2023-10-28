Defines the executable that will run when the container starts. It's like setting the default application that will handle all commands sent to the container. When you use `docker run <image> <command>`, `<command>` gets appended to the `ENTRYPOINT`.

Allows the container to run as a executable.

ENTRYPOINT ["executable", "param1", "param2"]

#docker #container 