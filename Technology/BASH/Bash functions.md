```bash
#!/bin/bash

hello_world () {
   echo 'hello, world'
}

hello_world

# returning values

#!/bin/bash

my_function () {
  echo "some result"
  return 55
}

my_function
echo $?

# parameters

#!/bin/bash

greeting () {
  echo "Hello $1"
}

greeting "Joe"
```

#bash