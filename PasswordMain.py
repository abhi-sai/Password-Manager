from cmd import Cmd
import PasswordManager


class MyPrompt(Cmd):

    def preloop(self):
        PasswordManager.checkFile()

    def do_create(self, args):
        """Creates new password for the service. Syntax - create Service """
        PasswordManager.create(args.split()[0])

    def do_add(self,args):
        """Add existing password for a service. Syntax - add Service Password"""
        if len(args.split()) < 2:
            print("Need 2 inputs")
        else:
            service, password = args.split()
            PasswordManager.add(service,password)

    def do_edit(self, args):
        """Edits password for service. Syntax - edit Service"""
        service, password = args.split()
        PasswordManager.create(service, password)

    def do_get(self, args):
        """Gets password for service. Syntax - get Service"""
        PasswordManager.get(args)

    def do_remove(self, args):
        """Removes password for service. Syntax - remove Service"""
        PasswordManager.remove(args)

    def do_list(self, args):
        """Lists all passwords. Syntax - list"""
        PasswordManager.printAllPasswords()

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting.")
        raise SystemExit


if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.prompt = '> '
    prompt.cmdloop('Starting prompt...')
    PasswordManager.checkFile()
