
### Concepts

By default Compose sets up a single network for you app. All services in Compose are discoverable by the service's name.

**Specify custom networks**

Each service can specify what networks to connect to with the service-level `networks` key, which is a list of names referencing entries under the top-level `networks` key.

```yaml
services:
	proxy:
		build: ./proxy
		networks:
			- frontend

	app:
		build: ./app
		networks:
			- frontend
			- backend

	db:
		image: postgres
		networks:
			- backend

networks:
	frontend:
		driver: custom-driver-1
	backend:
		driver: custom-driver-2
		driver_opts:
			foo: "1"
			bar: "2"
```

It's possible to provide custom name to the networks:

```yaml
services:
  # ...
networks:
  frontend:
    name: custom_frontend
    driver: custom-driver-1
```

Instead of, or as well as, specifying your own networks, you can also change the settings of the app-wide default network by defining an entry under `networks` named `default`:

```yaml
services:
  web:
    build: .
    ports:
      - "8000:8000"
  db:
    image: postgres

networks:
  default:
    # Use a custom driver
    driver: custom-driver-1
```

**Use a pre-existing network**

If you want your containers to join a pre-existing network, use the `external` option.

```yaml
services:
  # ...
networks:
  network1:
    name: my-pre-existing-network
    external: true
```

#container #docker #dockercompose