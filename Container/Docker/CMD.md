The main purpose is provide a default way to execute the container.
Can exists only one CMD instruction in Dockerfile.

The `CMD` instruction has three forms:

- `CMD ["executable","param1","param2"]` (_exec_ form, this is the preferred form)
- `CMD ["param1","param2"]` (as _default parameters to ENTRYPOINT_)
- `CMD command param1 param2` (_shell_ form)

#docker 