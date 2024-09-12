#!/usr/bin/python3
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
