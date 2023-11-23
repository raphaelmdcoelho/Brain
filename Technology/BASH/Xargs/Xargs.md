
`xargs` is a command-line utility that reads items from standard input (or from a provided file) and executes a given command using those items as arguments. The items are typically separated by whitespace or newline characters.

```bash
find . -name "*.txt" | xargs rm

grep -rl "apple" . | xargs wc -l

cat users.txt | awk '{print $1}' | xargs -I {} usermod -aG developers {}
```

```bash
for number in {1..5}; do echo "hello $number" > file$number.txt; done

find /home/raphaelcoelho -type f -name "*.txt" -not -path "/home/raphaelcoelho/.*/*"

 ~ find /home/raphaelcoelho -type f -name "*.txt" -not -path "/home/raphaelcoelho/.*/*" | xargs cat
 
find /home/raphaelcoelho/teste1 -type f -name "*.txt" -not -path "home/raphaelcoelho/.*" | xargs cat | awk "/1/ {print}"
```

#bash 