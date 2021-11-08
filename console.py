#!/usr/bin/python3
'''
'''
import cmd
import models
from models.base_model import BaseModel

dict_of_classes = {'BaseModel': BaseModel}


class HBNBCommand(cmd.Cmd):
    '''
    '''
    prompt = "(hbnb) "

    def do_EOF(self, line):
        '''End of file, exits'''
        return True
    
    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def emptyline(self):
        return cmd.Cmd.emptyline(self)

    def do_create(self, args):
        ''' create '''
        try:
            arguments = args.split()
            if len(arguments) == 0:
                print("** class name missing **")
                return False
            if arguments[0] in dict_of_classes:
                obj = dict_of_classes[arguments[0]]()
            else:
                print("** class doesn't exist **")
                return False
            print(obj.id)
            obj.save()
        except Exception:
            raise

    def do_show(self, args):
        ''' show an instance '''
        arguments = args.split()
        if len(arguments) == 0:
            print("** class name missing **")
            return False
        if arguments[0] not in dict_of_classes:
            print("** class doesn't exist **")
            return False
        if len(arguments) < 2:
            print("** instance id missing **")
            return False
        key = "{}.{}".format(arguments[0], arguments[1])
        st = models.storage.all()
        if key not in st:
            print("** no instance found **")
            return False
        print(st[key])


if __name__ == '__main__':
    HBNBCommand().cmdloop()