* `NGINX` has one master process and several work processes.
* The main purpose of the `master process` is to read and evaluate `configuration`, and maintain work processes.
* `Work processes` do actual processing of requests.
* The way NGINX and its modules work is determined in the `configuration file`.
* By default the configuration file is named as `nginx.conf` and placed in the directory  `/usr/local/nginx/conf`, `/etc/nginx` or `/usr/local/etc/nginx`
## Starting, Stopping, and Reloading Configuration

* To start NGINX, run the executable file.

```bash
nginx -s signal
```

* **stop**: fast shutdown.
* **quit**: graceful shutdown.
* **reload**: reloading the configuration file.
* **reopen**: reopening the log files.

* Once the master process receives the signal to reload configuration, it checks the syntax validity of the new configuration file and tries to apply the configuration provided in it.

## Configuration File's Structure

* Nginx consists of `modules` which are controlled by `directives` specified in the configuration file.
* Directives are divided into ***simple**** directives and ***block*** directives.
* The `simple` directive consists of the `name` and `parameters` separated by spaces and ends with a semicolon.
* A `block` directive has the same structure as a simple directive, but instead of the semicolon it ends with a set of additional instructions surrounded by braces.
* If the `block directive` can have other directives inside braces, it is called a context.
* Directives placed in the configuration file outside of any contexts are considered to be in the main context. The `events` and `http` directives reside in the `main` context, `server` in `http`, and `location` in `server`.

## [[NGINX Static Content]]

## [[NGINX Proxy Server]]


#server #nginx


