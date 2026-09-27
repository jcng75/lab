# Routing in Networking

While you can communicate between devices within the same local networking with switching, how does communication work between devices on other networks?

Routing handles this process, typically using a router to **route** data between different networks based on IP addresses.

`route # Display the current routing table`

`ip route add 192.168.2.0/24 via 192.168.1.1 # Add a route to the 192.168.2.0/24 network via the gateway 192.168.1.1`
## **NOTE: This needs to be done both ways**
`ip route add 192.168.1.0/24 via 192.168.2.1 # Add a route to the 192.168.1.0/24 network via the gateway 192.168.2.1`

`ip route add default via 192.168.1.1 # Add a default route via the gateway 192.168.1.1`
