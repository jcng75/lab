# IP Forwarding in Networking

Say we have the following scenario:

```
[Machine A - 192.168.1.5] <-> [Router - 192.168.1.0/24] <-> [Machine B] <-> [Router - 192.168.2.0/24] - [Machine C - 192.168.2.5]
```

When trying to run the command:

```
ping 192.168.2.5
```
# This will fail initially as the IP routes have not been configured
```
ip route add 192.168.2.0/24 via 192.168.1.6 # Add a route to the 192.168.2.0/24 network via the gateway 192.168.1.1
ip route add 192.168.1.0/24 via 192.168.2.1 # Add a route to the 192.168.1.0/24 network via the gateway 192.168.2.1
```

After configuring the routes, you would still fail as Linux by default does not enable IP forwarding.

```
# By default
cat /proc/sys/net/ipv4/ip_forward
0

# To enable IP forwarding temporarily
echo 1 > proc/sys/net/ipv4/ip_forward

# To do it permanently, the sysctl configuration needs to be updated
sysctl -w net.ipv4.ip_forward=1
echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.conf
```
