#!/usr/bin/python3
"""console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """quit"""
        return True

    def do_EOF(self, arg):
        """exit"""
        return True

    def do_help(self, arg):
        """help"""
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """do nothing"""
        pass

    def do_create(self, arg):
        """create"""
        if not arg:
            print('** class name missing **')
            return
        if arg not in globals():
            print("** class doesn't exist **")
            return
        new = globals()[arg]()
        new.save()
        print(new.id)

    def do_show(self, arg):
        """show"""
        args = arg.split()
        if not args:
            print('** class name missing **')
            return
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print('** instance id missing **')
            return
        allins = storage.all()
        key = f'{args[0]}.{args[1]}'
        if key not in allins:
            print('** no instance found **')
        else:
            print(allins[key])

    def do_destroy(self, arg):
        """destroy instances"""
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
