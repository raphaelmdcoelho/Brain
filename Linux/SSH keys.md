***Login into a server***
- ssh user@server-address

***Generate key***
- ssh-keygen (Gera duas chaves, privada e pública, por padrão na ~/.ssh

***ADD public key to server***
- ssh-copy-id -i /home/chaves/.ssh/nome-chave_key.pub root@10.1.1.79

***Notes***
- When trying to access the server for the first time trough ssh key, the server will asks a password, but not the user server passaword but the password provided when createling the key.

***References***

- https://youtu.be/NqW-BeYRBkE

#linux 