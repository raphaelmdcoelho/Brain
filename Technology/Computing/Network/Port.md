### Concepts

A port is **not** a physical connection.

It's a `logical connection` that's used by programs and services to exchange information.

It specifically determines which program or service on a computer or server that is going to be used.

**Range**
`0 - 65535`

Common port numbers.

`80, 443` - Web pages (HTTP, HTTPS)
`21` - FTP (File Transfer Protocol)
`25` - Email (SMTP)

A port is always **associated** with an **IP** address.

❗️**Easy explanation**: An `IP address` determines the location of that server. Then the `port` number determines which service or program on that server it wants to use.

### Tools

**Netstat (Network Statistics)**:  Command line tool that is used to display the current network connections and port activity on your computer.

Display addresses and port numbers in numerical form:

```bash
netstat -n
```

#network #computing 