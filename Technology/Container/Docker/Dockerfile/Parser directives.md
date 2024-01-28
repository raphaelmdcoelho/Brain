### Concepts

Parser directives are optional, and effect the way in which subsequent lines in a Dockerfile are handled. Parser directives are written as a special type of comment in the form `# directive=value`. A single directive may only be used once.

The following parser directives are supported:

* syntax
* escape

### Examples

```dockerfile
# syntax=docker/dockerfile:1
# escape=`
```

#docker #container #dockerfile