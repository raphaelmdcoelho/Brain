### Concepts

You can use `.dockerignore` file to exclude files and directories from the build context.

**Negating matches**

You can prepend lines with a `!` (exclamation mark) to make exceptions to exclusions. The following is an example `.dockerignore` file that uses this mechanism:

```gitignore
*.md
!README.md
```

#docker #container #dockerfile