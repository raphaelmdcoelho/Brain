```
for l in ./files/*.txt; do echo "message"; done
```

```
#!/bin/bash
for f in *
	do 
		if [[ $f == *.txt ]]
			then 
				echo "$f" 
	fi done
```

#bash 