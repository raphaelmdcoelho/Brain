
## Concepts

* It's stands for Secure SHell.
* Cryptographic network protocol.
* During the comunication between client and server using ssh keys, the server stores the public key and the client use to have the private key. This is possible because everything encrypted with public key can be only decrypted with private key.

## Operation

***Login into a server***
- ssh user@server-address

***Generate key***
- ssh-keygen (Gera duas chaves, privada e pública, por padrão na ~/.ssh

***Add public key to server***
- ssh-copy-id -i /home/chaves/.ssh/nome-chave_key.pub root@10.1.1.79

***SSH config file***
* /etc/ssh/sshd_config

***Restart***
* systemctl restart ssh

***Notes***
- When trying to access the server for the first time trough ssh key, the server will asks a password, but not the user server passaword but the password provided when createling the key.

## References

- https://youtu.be/NqW-BeYRBkE

#linux #ssh 