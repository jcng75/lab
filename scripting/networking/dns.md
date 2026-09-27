# DNS in Networking

DNS is used to translate human-readable domain names (i.e example.com) into IP addresses that computers can understand.

For example, let's say that you would like to name a server domain name db.  To do so, you would need to create a record in the hosts file:
```
cat ... >> /etc/hosts
192.168.1.11   db
```

`hostname` - Displays the current hostname of the machine.
# hostname -> ip address == Name resolution

This becomes quite complex once you have multiple machines and need to manage domain name resolution across a network, which is where DNS servers come into play.
Instead of editing the files now, we can add the IP of the dns server to the `/etc/resolv.conf` file:
```
nameserver 192.168.1.1
```

DNS Resolution Precedence:
1. `/etc/hosts` file
2. DNS server specified in `/etc/resolv.conf`
3. Forward the remaining queries to the next DNS server in the chain

NOTE: This can be switched depending on the nsswitch configuration in `/etc/nsswitch.conf`. The `hosts` line in this file determines the order in which name resolution is performed. For example:
```
hosts: files dns
```
