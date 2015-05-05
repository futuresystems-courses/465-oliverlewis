from cloudmesh_base.Shell import Shell
import subprocess


class command_apachestorm(object):

    @classmethod
    def status(cls, host):
        msg = "Unknown host"
        try:
            msg = Shell.ping("-c", "1", host)
        except:
            pass
        if "1 packets transmitted, 1 packets received" in msg:
            return True
        elif "Unknown host" in msg:
            return False
        else:
            return False
    
    @classmethod
    def start(cls, serverName):
        try:
            #pip.main(['install', packageName])
	    print "starting server : ", serverName
            subprocess.call("eval `ssh-agent -s`", shell=True)
            subprocess.call("ssh-add ~/.ssh/oliver-cloudmesh-india", shell=True)
            return_code = subprocess.call("ansible-playbook -i inventory.txt -c ssh zookeeper-nimbus.yaml", shell=True)
        except:
            pass

    @classmethod
    def stop(cls, serverName):
        try:
            #pip.main(['install', packageName])
	    print "stopping server : ", serverName
        except:
            pass

    @classmethod
    def deploy(cls, nimbusNode, zookeeperNode, supervisorNodes):
        try:
            print nimbusNode, zookeeperNode, supervisorNodes
        except:
            pass
