## Concept

At linux o, each file is associated with a **group** and a **owner**. Chown stands for *change owner*. 

* check permissions:
```bash
ls -l
```

* base command to change file user:
```bash
# chown usuario file
chown newuser file.txt
```

* base command to change file group:
```bash
# chown usuario[:grupo] file
chown newuser:newgroup file.txt
chown :newsgroup file.txt
```

#linux 