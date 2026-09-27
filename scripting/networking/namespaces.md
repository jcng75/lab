# Networking Namespaces

Networking namespaces are a feature in the Linux kernel that allow you to isolate network resources such as interfaces, IP addresses, routing tables, and firewall rules. Each network namespace has its own network stack, which means processes in different namespaces can have overlapping IP addresses and independent network configurations.

## Creating and Using Network Namespaces

You can create a new network namespace using the `ip` command:

```bash
sudo ip netns add red
sudo ip netns add blue
```

To list all network namespaces:

```bash
ip netns list
```

To run a command in a specific network namespace:

```bash
sudo ip netns exec red <command>
```

For example, to start a shell in the new namespace:

```bash
sudo ip netns exec red bash
```

Alternatively, you can do the following:
```bash
sudo ip -n red link
```

Now that we have created the network namespaces, you can start configuring network interfaces and setting up communication between them.
```bash
# Created a veth (virtual Ethernet) pair to connect the red and blue namespaces
ip link add veth-red type veth peer name veth-blue
ip link set veth-red netns red
ip link set veth-blue netns blue

# Assign IP addresses to the veth interfaces
ip -n red addr add 192.168.15.1 dev veth-red
ip -n blue addr add 192.168.15.2 dev veth-blue

# Bring up the loopback interfaces in each namespace
ip -n red link set veth-red up
ip -n blue link set veth-blue up
```

## Deleting a Network Namespace

To delete a network namespace:

```bash
sudo ip netns delete mynamespace
```
