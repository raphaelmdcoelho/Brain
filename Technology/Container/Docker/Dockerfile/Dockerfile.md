### Concepts

**Format**

```Dockerfile
# Comment
INSTRUCTION arguments
```

The Dockerfile **must begin with a `FROM` instruction. This may be after `parser directives`, `comments` and globally scoped `ARG`s.

The `Dockerfile` should be in UTF-8 format, if not during build process you can receive the following error message:

`ERROR: failed to solve: Internal: Internal: Internal: stream terminated by RST_STREAM with error code: INTERNAL_ERROR`

These are some of the instructions from dockerfile:

* [[Parser directives]]
- [[FROM]]
- [[WORKDIR]]
- [[RUN]]
- COPY
- EXPOSE
- [[CMD]]
- [[ENV]]
- [[ADD]]
- [[VOLUME]]
- [[ENTRYPOINT]]
- [[USER]]
- [[ARG]]

**[[Environment replacement]]**
**[[dockerignore]]**
**[[Shell and exec form]]**

#docker #container 
