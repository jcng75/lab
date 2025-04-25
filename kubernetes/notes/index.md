# Notes
- Instead of going into the kubernetes documentation from the start, try using the resources inside kubectl
- By running `kubectl [command] --help | vim -`, you can most likely find the information before searching it up online
- When generating template kubernetes yaml files (i.e deployments), this can be done by using the --dry-run command
- For example: `kubectl create deployment test --dry-run=client -o yaml > deployment.yaml`

- Kubernetes is considered the OS of the cloud.  Think of the nodes as a bunch of virtual machines who communicate with each other
- A control plane is what manages the scheduling, api calls, key value store (etcd), and management of nodes
- Pods are the smallest unit that exist inside within each node 
    - Pods are NOT just the container.  Each pod is an operating envrionment that has the ability to run one or more containers.
- Each node contains a kubelet that communicates with the control plane to provide health information on pod information
    - Additionally, they also contain a kube-proxy that allows them into maintain network rules on each node

## Networking
- Each pod gets its own IP address
- By default pods can connect to all pods on all nodes
    - This can be limited through network policies
- Containers in pods can communicate with each other through localhost
- Each container must have their own unique port
- The CNI Plugin is a Container Networking Interface
    - Think of this plugin as a physical network card
    - It also handles the wiring the connections between each container
    - IP addresses are assigned and routes are set up using IPTables on nodes
    - Plugins: Cilium, Calico, Flannel
- To investigate the node vm's CNI, we used rdctl (rancher-desktop ctl): `rdctl shell bash`
- We then checked out /etc/cni/net.d/
- We saw the file 10-flannel.conflist and by using `cat` we observed that flannel was running on our cluster
