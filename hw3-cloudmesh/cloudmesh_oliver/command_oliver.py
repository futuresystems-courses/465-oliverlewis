from cloudmesh_base.Shell import Shell
import pip

class command_oliver(object):

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
    def install(cls, packageName):
	try:
	    pip.main(['install', packageName])
	except:
	    pass
    @classmethod
    def start(cls, serverName):
        try:
            #pip.main(['install', packageName])
	    print "starting server : ", serverName
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
    def run(cls, server):
        try:
            #pip.main(['install', packageName])
	    print "Running server : ", server
        except:
            pass


