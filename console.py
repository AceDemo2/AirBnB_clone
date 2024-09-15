#!/usr/bin/python3
"""console"""
import cmd
from models import storage
import json

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
        """create instance"""
        if not arg:
            print('** class name missing **')
            return
        if arg not in storage.classes():
            print("** class doesn't exist **")
            return
        new = storage.classes()[arg]()
        new.save()
        print(new.id)

    def do_show(self, arg):
        """show"""
        args = arg.split()
        if not args:
            print('** class name missing **')
            return
        if args[0] not in storage.classes():
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
        args = arg.split()
        if not args:
            print('** class name missing **')
            return
        if args[0] not in storage.classes():
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
            del allins[key]
            storage.save()

    def do_all(self, arg):
        """print instances"""
        allins = storage.all()
        obj = []
        if not arg:
            for v in allins.values():
                obj.append(str(v))
        else:
            
            if arg not in storage.classes():
                print("** class doesn't exist **")
                return
            else:
                for k, v in allins.items():
                    if arg == k.split('.')[0]:
                        obj.append(str(v))
        print(obj)

    def do_count(self, arg):
        """count instances"""
        if arg not in storage.classes():
            print("** class doesn't exist **")
            return
        allins = storage.all()
        count = 0
        for k in allins:
            if arg == k.split('.')[0]:
                count += 1
        print(count)

    def default(self, arg):
        """unrecognized commands"""
        args = arg.split('.')
        if len(args) == 2:
            funcs = {'all': self.do_all,
                    'count': self.do_count,
                    'show': self.do_show,
                    'destroy': self.do_destroy,
                    'update': self.do_update}
            func = args[1].replace("(", "").replace(")", "")
            if 'update' in func or 'show' in func or 'destroy' in func:
                dic = False
                if 'update' in func:
                    if '{' in func:
                        sfunc = func.split('"', 1)
                        sfunc[1] = sfunc[1].replace('",', '')
                        dic = True
                    else:
                        sfunc = func.replace(',', '').split('"', 1)
                        
                else:
                    sfunc = func.split('"', 1)
                if len(sfunc) > 1 and '{' not in func:
                    sfunc[1] = sfunc[1].replace('"', '')
                if len(sfunc) > 1:    
                    name = f'{args[0]} {sfunc[1]}'
                else:
                    name = f'{args[0]}'
                func = sfunc[0]
            else:
                return
            if not dic:
                funcs[func](name)
            else:
                funcs[func](name, dic) 

    def do_update(self, arg, dic=False):
        """updates an instance"""
        args = arg.split()
        if not args:
            print('** class name missing **')
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print('** instance id missing **')
            return
        allins = storage.all()
        key = f'{args[0]}.{args[1]}'
        if key not in allins:
            print('** no instance found **')
            return
        ins = allins[key]
        if not dic:
            if len(args) < 3 and not dic:
                print('** attribute name missing **')
                return
            if len(args) < 4 and not dic:
                print('** value missing **')
                return
            name = args[2]
            value = args[3].strip('"')
            self.assign_attr(ins, name, value)
        elif dic:
            dic_attr = eval(args[2])
            if not isinstance(dic_attr, dict):
                return
            for name, value in dic_attr.items():
                self.assign_attr(ins, name, value)
        ins.save()

    def assign_attr(ins, name, value):
        if hasattr(ins, name):
            ty = type(getattr(ins, name))
            value = ty(value)
        else:
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    pass
        setattr(ins, name, value)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
