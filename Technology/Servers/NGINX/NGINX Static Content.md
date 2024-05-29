```nginx
http {
	server {
		location / {
			root /data/www;
		}
		
		location /images/ {
			root /data;
		}
	}
}
```

**Note**: In case something does not work as expected, you may try to find out the reason in `access.log` and `error.log` files in the directory `/usr/local/nginx/logs` or `/var/log/nginx`.

#server #nginx