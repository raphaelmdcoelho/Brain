The main purpose is provide a default way to execute the container.
Can exists only one CMD instruction in Dockerfile.

Specifies arguments that will be fed into the `ENTRYPOINT`. If `ENTRYPOINT` is not explicitly set, `CMD` will act as the executable, but only if you don't override it with the `docker run <command>` command-line argument.

The `CMD` instruction has three forms:

- `CMD ["executable","param1","param2"]` (_exec_ form, this is the preferred form)
- `CMD ["param1","param2"]` (as _default parameters to ENTRYPOINT_)
- `CMD command param1 param2` (_shell_ form)

#docker #container 