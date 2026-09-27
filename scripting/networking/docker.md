# Docker Networking

There are a few types of networking for Docker containers.  Let's go over the different types:

## Scenario
Let's consider you have a local machine running docker and an IP address of 192.168.1.10 running on network interface eth0.


The `none` network disables all networking for the container.
Such containers cannot communicate with other containers or the outside network.
```bash
docker run --network none nginx
```

The `host` network allows the container to share the host's network.  If we were to host a web server in this container on port 80, the service would be accessible directly via the host's IP address, in this case, 192.168.1.10:80.
```bash
docker run --network host nginx
docker run --network host nginx # Would fail as port 80 is already in use by first container
```

The `bridge` network is the default network for Docker containers.
The bridge network is like an interface to the host, but a switch to the namespaces/containers within the host.

When docker runs, it creates a default bridge network named `bridge` on the host machine.  NOTE: While it is called bridge in docker namespaces, you can identify it as a network interface on the host machine, typically named `docker0`, using a similar technique to namespace networking (`ip link add docker0 type bridge`).
```bash
docker run --network bridge nginx
docker run nginx # Would use the default bridge network
```

In this context, containers and network namespaces are the same, as each container has its own network namespace, isolated from the host and other containers being put on the same bridge network.

If you try to view the container's hosted webpage from within the network host, you would be able to view the page using the container's IP address on the bridge network.  You can find the container's IP address by running:
```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_id>
```
Users who try to curl the IP outside of the local host would not be able to reach the container.  To handle this, Docker allows us to expose a port on the host and map it to the container's port.
```bash
docker run -p 8080:80 nginx
```
In this example, port 8080 on the host is mapped to port 80 in the container.  You can now access the container's web server from the host or any other machine on the network using `http://192.168.1.10:8080`.
