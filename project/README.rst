Dev-ops for Apache Storm on Openstack
========================================

Pre-requisites required for setup
-----------------------------------

I’ll be using a 3 node Openstack network on FutureSystems. (Note this is configurable and scalable.)

Node 1: Will contain the Zookeeper server and Storm Nimbus node
Node 2 & 3: Will be the supervisor nodes.
    
1. Must be familiar with the terminal.
2. Must have access to FutureSystems and provision 3 VM's through the FutureSystems interface.
3. Must assign the machines with a public IP address. This is necessary for the Nimbus node to view the Storm UI. 
4. Open port 8080 on the Nimbus node. This is done by changing the security group and enabling 8080 port access.
5. Must have git installed. install `git <http://git-scm.com/book/en/v2/Getting-Started-Installing-Git>`_.
6. Must have ansible installed. install `ansible <http://docs.ansible.com/intro_installation.html>`_.

Source code 
-------------

The source code for the apache storm commad can be browed at

* https://github.com/futuresystems/465-oliverlewis/tree/master/cloudmesh_apachestorm

Setup instructions with cloudmesh
----------------------------------

::

    git clone https://github.com/futuresystems/465-oliverlewis.git
    cd cloudmesh_apachestorm
    python setup.py install
    
Now edit the file ~/.cloudmesh/cmd3.yaml and add the line::

   - cloudmesh_apachestorm.plugins
   
in the module list. Now you are ready to use it. To simplify password management we recommend that you use ssh agent::

    eval `ssh-agent -s`
    ssh-add ~/.ssh/<key-used-to-create-vm's>
    
Next you can start the cloudmesh shell and the apachestorm command will be available::

    cm
    
Command
-------------
:Usage:
    | apachestorm COMMAND
    | apachestorm COMMAND --stormTtl=TIMETOLIVE
    | apachestorm COMMAND --nimbusNode=NIMBUSNODE --zookeeperNode=ZOOKEEPERNODE --supervisorNodes=<SUPERVISORNODES>...
:Arguments:
    | COMMAND          deploy, start, stop commImand
    | TIMETOLIVE       storm alive time
    | NIMBUSNODE       storms nimbus node ip address
    | ZOOKEEPERNODE    zookeeper nodes ip address
    | SUPERVISORNODES  supervisornode ip addresses 
 
Apache Storm UI interface
--------------------------

* Go the the public ip address of the nimbus node and use port 8080 to view the UI.

Example Deployment
-------------------

In this example we will 
    - First deploy Apache Storm on the nodes.
    - Start Apache Storm
    - Stop Apache Storm
    
Note the nodes must be the the nodes you have created using your key.
::

   cm apachestorm deploy --nimbusNode=10.23.1.220 --zookeeperNode=10.23.1.220 --supervisorNode=10.23.1.217 --supervisorNode=10.23.1.218
   cm apachestorm start --stormTtl=600
   cm apachestorm stop
   
Describe wht you do and put the concrete commands there.
use $variables in the above and use export command to assign them assuming you use bash

Example Usage
---------------

Put here a simple example in on how to use storm as to verify that the deployment works
