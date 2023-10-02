### List all users
```bash
awk -F':' '{ print $1}' /etc/passwd
```

### Get user ID
```bash
id username
```

### Add user
```bash
sudo useradd username
```


### Add password to a existing user

```bash
passwd username
```

### Accessing user configuration file

```bash
cat /etc/passwd
```

### Change the user login name
```bash
sudo usermod -l new_login_name old_login_name
```


#linux 
