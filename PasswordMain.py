from cmd import Cmd
import PasswordManager
from loginAuth import loginAuthentication

class MyPrompt(Cmd):

    def preloop(self):
        if loginAuthentication() is False:
            print("Quitting.")
            raise SystemExit

    def do_create(self,args):
        """Creates new password for the service. Syntax - create """
        PasswordManager.create()

    def do_add(self,args):
        """Add existing password for a service. Syntax - add """
        PasswordManager.add()

    def do_edit(self, args):
        """Edits password for service. Syntax - edit """
        PasswordManager.edit()

    def do_get(self, args):
        """Gets password for service. Syntax - get """
        PasswordManager.get()

    def do_remove(self, args):
        """Removes password for service. Syntax - remove """
        PasswordManager.remove()

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting.")
        raise SystemExit


if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.prompt = '> '
    prompt.cmdloop('Starting prompt...')
