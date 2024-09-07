
## Concept

It is an all-around cryptography library that offers an open-source application of the [[TLS]] protocol. It allows users to perform various SSL-related tasks, including CSR (Certificate Signing Request) generation, private keys, generation and SSL certificate installation.

## Usage

### Http request

```bash
openssl s_client -connect www.google.com:443

GET /search?q=k8s HTTP/1.1
Host: www.google.com
```

```bash
echo -e 'GET / HTTP/1.1\r\nHost: www.google.com\r\nConnection: close\r\n\r\n' | openssl s_client -connect www.google.com:443 -quite
```

**Note**: the `-e` flag on `echo` command allows echo to perform the interpretation of escape sequences in the string. 

#technology #computing #shell 