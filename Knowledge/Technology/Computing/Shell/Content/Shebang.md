
## Concept

It's a notation (`#!`) to be added to a very beginning of a file, so shell will know which binary to choose when running the script

## Syntax

```bash
# bash file:

#!/bin/bash -> shebang referencing a bash binary
echo "Message"
```

```bash
# python script:

#!/usr/bin/python

print "Message"
```

## How it works

When the file is executed, it calls the binary with the file as an argument, as shown here:

**Calling like `./display-message.sh`

```bash
/bin/bash ./display-message.sh
```

**Calling like `/tmp/display-message.sh`

```bash
/bin/bash /tmp/display-message.sh
```

## Summary

```bash
#!/bin/bash
```

#technology #computing #shell 