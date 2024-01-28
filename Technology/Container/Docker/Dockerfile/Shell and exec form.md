### Concepts

The `RUN`, `CMD`, and `ENTRYPOINT` instructions all have two possible forms:

- `INSTRUCTION ["executable","param1","param2"]` (exec form)
- `INSTRUCTION command param1 param2` (shell form)

The exec form makes it possible to avoid shell string munging, and to invoke commands using a specific command shell, or any other executable. It uses a JSON array syntax, where each element in the array is a command, flag, or argument.

The shell form is more relaxed, and emphasizes ease of use, flexibility, and readability. The shell form automatically uses a command shell, whereas the exec form does not.

### Exec form

The exec form is parsed as a JSON array, which means that you must use double-quotes (") around words, not single-quotes (').

```Dockerfile
ENTRYPOINT ["/bin/bash", "-c", "echo", "hello"]
```

The exec form is best used to specify an `ENTRYPOINT` instruction, combined with `CMD` for setting default arguments that can be overridden at runtime.

**Variable substitution**

Using the exec form doesn't automatically invoke a command shell. This means that normal shell processing, such as variable substitution, doesn't happen. For example, `RUN [ "echo", "$HOME" ]` won't handle variable substitution for `$HOME`.

If you want shell processing then either use the shell form or execute a shell directly with the exec form, for example: `RUN [ "sh", "-c", "echo $HOME" ]`. When using the exec form and executing a shell directly, as in the case for the shell form, it's the shell that's doing the environment variable substitution, not the builder.

**Backslashes**

In exec form, you must escape backslashes. This is particularly relevant on Windows where the backslash is the path separator. The following line would otherwise be treated as shell form due to not being valid JSON, and fail in an unexpected way:

```dockerfile
RUN ["c:\windows\system32\tasklist.exe"]
```

The correct syntax for this example is:

```dockerfile
RUN ["c:\\windows\\system32\\tasklist.exe"]
```

### Shell form

Unlike the exec form, instructions using the shell form always use a command shell. The shell form doesn't use the JSON array format, instead it's a regular string. The shell form string lets you escape newlines using the [escape character](https://docs.docker.com/engine/reference/builder/#escape) (backslash by default) to continue a single instruction onto the next line. This makes it easier to use with longer commands, because it lets you split them up into multiple lines. For example, consider these two lines:

```dockerfile
RUN source $HOME/.bashrc && \
echo $HOME
```

They're equivalent to the following line:

```dockerfile
RUN source $HOME/.bashrc && echo $HOME
```

You can also use ==heredocs== with the shell form to break up a command:

```dockerfile
RUN << EOF
source $HOME/.bashrc && \
echo $HOME
EOF
```

**Use a different shell**

You can change the default shell using the `SHELL` command. For example:

```dockerfile
SHELL ["/bin/bash", "-c"]
RUN echo hello
```

#docker #container #dockerfile