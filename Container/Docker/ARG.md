The `ARG` instruction defines a variable that users can pass at build-time to the builder with the `docker build` command using the `--build-arg <varname>=<value>` flag. If a user specifies a build argument that was not defined in the Dockerfile, the build outputs a warning.

FROM busybox
USER ${username:-some_user}
ARG username
USER $username

docker build --build-arg username=what_user .

#docker 