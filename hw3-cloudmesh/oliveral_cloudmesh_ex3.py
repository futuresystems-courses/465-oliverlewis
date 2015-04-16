import cloudmesh


def start_vm():
	print cloudmesh.shell("vm start --cloud=india --image=futuresystems/ubuntu-14.04 --flavor=m1.small --name={0}".format("oliveral-supervisor3"))

def stop_vm(name):
	cloudmesh.shell("vm delete {0} --cloud=india --force".format(name))


decision=raw_input('Enter \'start\' or \'stop\' to start/stop VM : ')

if (decision.lower() == "start"):
	start_vm()
elif(decision.lower() == "stop"):
	name = raw_input("Enter vm name to stop: ")
	stop_vm(name)
else:
	print "Enter correct option: start/stop."
