# Switching in Networking

ip link # Display all network interfaces and their statuses
ip addr add 192.168.1.100/24 dev eth0 # Assign an IP address to a network interface - dev (device)

ping 192.168.1.11 # Test connectivity to another host on the network

Switching can be seen as the process of connecting machines within a **local** network, using network switches to forward data within the network based on MAC addresses.
