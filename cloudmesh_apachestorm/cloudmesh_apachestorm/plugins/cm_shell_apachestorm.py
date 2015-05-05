from __future__ import print_function
import os
from cmd3.console import Console
from cmd3.shell import command

from cloudmesh_apachestorm.command_apachestorm import command_apachestorm


class cm_shell_apachestorm:

    def activate_cm_shell_apachestorm(self):
        self.register_command_topic('mycommands', 'apachestorm')

    @command
    def do_apachestorm(self, args, arguments):
        """
        ::

          Usage:
              apachestorm COMMAND
              apachestorm deploy --nimbusNode=NIMBUSNODE --zookeeperNode=ZOOKEEPERNODE --supervisorNodes=SUPERVISORNODES...

          tests via ping if the host ith the give NAME is reachable

          Arguments:

            COMMAND          deploy, start, stop commImand
            deploy           deploy command
            NIMBUSNODE       storms nimbus node ip address
            ZOOKEEPERNODE    zookeeper nodes ip address
            SUPERVISORNODES  supervisornode ip addresses 

          Options:

             -v       verbose mode

        """
        #pprint(arguments)
        if arguments["COMMAND"] == "start":
            command_apachestorm.start(arguments["COMMAND"])
        if arguments["COMMAND"] == "stop":
            command_apachestorm.stop(arguments["COMMAND"])
        if arguments["deploy"] is not None:
            command_apachestorm.deploy(arguments["--nimbusNode"],arguments["--zookeeperNode"], arguments["--supervisorNodes"])


if __name__ == '__main__':
    command = cm_shell_apachestorm()
    command.do_apachestorm("iu.edu")
    command.do_apachestorm("iu.edu-wrong")
