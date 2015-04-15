import cloudmesh


def start_vm():
	print cloudmesh.shell("vm start --cloud=india --image=futuresystems/ubuntu-14.04 --flavor=m1.small --name={0}".format("oliveral-supervisor3"))

def terminate_vm():
	cloudmesh.shell("vm delete --group={0} --cloud=india --force".format("oliveral-supervisor2"))


decision=raw_input('Enter \'start\' or \'stop\' to start/stop VM : ')

if (decision.lower() == "start"):
	start_vm()
elif(decision.lower() == "stop"):
	stop_vm()
else:
	print "Enter correct option: start/stop."
