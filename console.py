#!/usr/bin/python3
"""console"""
import cmd
from models import storage

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
            if 'update' in func:
                sfunc = func.split(',', 2)
                if len(sfunc) == 3:
                    funcid = sfunc[0].split('"')
                    oid = funcid[0].strip()
                    aname = sfunc[1].strip().strip('"')
                    avalue = sfunc[2].strip().strip('"')
                    name = f'{args[0]} {oid} {aname} {avalue}'
                    func = 'update'
                else:
                    return
            elif 'show' in func or 'destroy' in func:
                sfunc = func.split('"')
                name = f'{args[0]} {sfunc[1]}' if len(sfunc) > 1 and sfunc[1] else f'{args[0]}'
                func = sfunc[0]
            elif func in funcs:
                name = args[0]
            else:
                return
            funcs[func](name)

    def do_update(self, arg):
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
        if len(args) < 3:
            print('** attribute name missing **')
            return
        if len(args) < 4:
            print('** value missing **')
            return
        ins = allins[key]
        name = args[2]
        value = args[3].strip('"')
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
        ins.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
