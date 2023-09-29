```bash
awk options 'selection _criteria {action }' input-file > output-file

awk '{ print }' ./file.txt

awk '/manager/ {print}' ./file.txt

awk '{print $1, $4}' ./file.txt
```

#bash 