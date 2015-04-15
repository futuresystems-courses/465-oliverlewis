from __future__ import print_function
import os
from cmd3.console import Console
from cmd3.shell import command

from cloudmesh_oliver.command_oliver import command_oliver


class cm_shell_oliver:

    def activate_cm_shell_oliver(self):
        self.register_command_topic('mycommands', 'oliver')

    @command
    def do_oliver(self, args, arguments):
        """
        ::

          Usage:
              oliver --name=NAME
	      oliver --install=INSTALL
	      oliver --start=SERVERNAME
	      oliver --stop=SERVERNAME
	      oliver --run=SERVER

          tests via ping if the host ith the give NAME is reachable

          Arguments:

            NAME      Name of the machine to test
	    INSTALL   pip intall the package name
	    SERVERNAME server name
 	    SERVER    Server that needs to be controlled

          Options:

             -v       verbose mode

        """
        # pprint(arguments)
	if arguments["--install"] is not None:
	    command_oliver.install(arguments["--install"])
	if arguments["--start"] is not None:
            command_oliver.start(arguments["--start"])
	if arguments["--stop"] is not None:
            command_oliver.stop(arguments["--stop"])
	if arguments["--run"] is not None:
            command_oliver.run(arguments["--run"])
        if arguments["--name"] is None:
            Console.error("Please specify a host name")

if __name__ == '__main__':
    command = cm_shell_oliver()
    command.do_oliver("iu.edu")
    command.do_oliver("iu.edu-wrong")
