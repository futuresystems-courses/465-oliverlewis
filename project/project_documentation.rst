=================
Dev-ops for Apache Storm on Openstack
=================

I’ll be using a 3 node Openstack network on FutureSystems. (Note this is configurable and scalable.)

Node 1: Will contain the Zookeeper server and Storm Nimbus node
Node 2 & 3: Will be the supervisor nodes.

-----------------
Pre-requisites required for setup

1. Must be familiar with the terminal.
2. Must have access to FutureSystems and provision 3 VM's through the FutureSystems interface.
3. Must assign the machines with a public IP address. This is necessary for the Nimbus node to view the Storm UI. 
4. Open port 8080 on the Nimbus node. This is done by changing the security group and enabling 8080 port access.
5. Must have git installed.
6. Must have ansible installed.
-----------------

-----------------
Deployment instructions without cloudmesh

1. git clone https://github.com/futuresystems/465-oliverlewis.git
2. cd project
3. edit the inventory file and enter the IP address's of the machines you started using FutureSystems. (At this time only 1 nimbus node and only 1 zookeeper node and N supervisor nodes are allowed)
4. edit the storm.yaml file and enter the IP address of the machine on which the nimbus node and zookeeper node will reside.
5. ansible-playbook -i inventory.txt -c ssh zookeeper-nimbus.yaml
-----------------

-----------------
Deployment instructions with cloudmesh

1. git clone https://github.com/futuresystems/465-oliverlewis.git
2. cd cloudmesh_apachestorm
3. edit the inventory file and enter the IP address's of the machines you started using FutureSystems. (At this time only 1 nimbus node and only 1 zookeeper node and N supervisor nodes are allowed)
4. edit the storm.yaml file and enter the IP address of the machine on which the nimbus node and zookeeper node will reside.
5. ansible-playbook -i inventory.txt -c ssh zookeeper-nimbus.yaml
-----------------

-----------------
Apache Storm UI interface
-----------------

* Go the the public ip address of the nimbus node and use port 8080 to view the UI.
