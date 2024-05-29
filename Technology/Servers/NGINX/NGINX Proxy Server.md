
This means a server that receives requests, passes them to the proxied servers, retrieves responses from them, and sends them to the clients.

```nginx
http {
	server {
		listen 8080;
		root /data/api;

		location / {
		}
	}

	server {
		location / {
			proxy_pass http://localhost:8080;
		}

		location /images/ {
			root /data;
		}
	}
}
```


#server #nginx