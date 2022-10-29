#!/usr/bin/python3
"""Defines the HBNB console"""
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Defines the command intepreter"""
    prompt = "(hbnb) "
    __classes = {
            "BaseModel": BaseModel,
            }

    def emptyline(self):
        """Does nothing when it receives an empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print("")
        return True

    def do_create(self, arg):
        """Creates a new instance of"""
        if not arg:
            print("** class name missing **")

        args = self.clean_args(arg)
        cls_name = args[0]
        if cls_name in self.__classes:
            _obj = self.__classes[cls_name]()
            print(_obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representration of an instance
        based on the class name and id.
        """
        if not arg:
            print("** class name missing **")
            return

        args = self.clean_args(arg)
        objdict = models.storage.all()
        clsname = args[0]

        try:
            if clsname in self.__classes:
                id = args[1]
                print(objdict["{}.{}".format(clsname, id)])
            else:
                print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the classname.
        """
        args = self.clean_args(arg)

        if len(args) > 0 and args[0] not in self.__classes:
                print("** class doesn't exist **")
        else:
            objdict = models.storage.all()
            newobj = []
            for obj in objdict.values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    newobj.append(obj.__str__())
                elif len(args) == 0:
                    newobj.append(obj.__str__())
            print(newobj) 

    def do_destroy(self, arg):
        """Deletes an instance based on the class name 
        and id
        """
        if not arg:
            print("** class name missing **")
            return

        args = self.clean_args(arg)
        cls_name = args[0]
        objects = models.storage.all()
        try:
            obj_id = args[1]
            if cls_name in self.__classes:
                _key = "{}.{}".format(cls_name, obj_id)
                obj = objects.pop(_key)
                del obj
                models.storage.save()
            else:
                print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    @staticmethod
    def clean_args(args: str):
        """
        clean arguments
        """
        args = args.strip().split(' ')
        return args


if __name__ == '__main__':
        HBNBCommand().cmdloop()
