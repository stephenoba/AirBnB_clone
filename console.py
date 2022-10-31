#!/usr/bin/python3
"""Defines the HBNB console"""
import cmd
import re

import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines the command intepreter"""
    prompt = "(hbnb) "
    __classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
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
        """
        Creates a new instance of

        Usage: |
            create <class name>
        """
        if not arg:
            print("** class name missing **")
            return

        args = self.clean_args(arg)
        cls_name = args[0]
        if cls_name in self.__classes:
            _obj = self.__classes[cls_name]()
            models.storage.save()
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

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name
        and id

        Usage: |
            destroy <class name> <id>
        """
        if not arg:
            print("** class name missing **")
            return

        args = self.clean_args(arg)
        cls_name = args[0]
        objects = models.storage.all()
        try:
            if cls_name in self.__classes:
                obj_id = args[1]
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

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        and can filter on class name

        Usage: |
            all
            all <class name>
        """
        objects = models.storage.all()
        if arg:
            if arg in self.__classes:
                args = self.clean_args(arg)
                objects = dict(filter(
                    lambda x: type(x[1]) == eval(args[0]),
                    objects.items()
                    ))
            else:
                print("** class doesn't exist **")
                return
        print(list(map(lambda x: str(x), objects.values())))

    def do_update(self, arg):
        """
        Updates an instance based on the class name an id

        Usage: |
            update <class name> <id> <attribute name> "<attribute value>"

        Example: |
            update BaseModel 1234-5678 name "Betty Holberton"
            update BaseModel 1234-5678 number "89"
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
                obj = objects.get(_key)
                if not obj:
                    print("** no instance found **")
                    return
                if len(args) < 3:
                    print("** attribute name missing **")
                    return
                if len(args) < 4:
                    print("** value missing **")
                    return
                attr = args[2]
                value = self.parse_attr_value(args[3], arg)
                if hasattr(obj, attr):
                    _type = type(getattr(obj, attr))
                    setattr(obj, attr, _type(value))
                else:
                    setattr(obj, attr, value)
                obj.save()
            else:
                print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")

    @staticmethod
    def parse_attr_value(arg: str, args_str: str):
        """"
        parse value containing spaces"
        """
        if arg.startswith('"'):
            res = re.search(
                    r'".+\s?(.+\s?)+?"', args_str)
            if res:
                arg = res.group()
            return arg.split('"')[1]
        return arg

    @staticmethod
    def clean_args(args: str):
        """
        clean arguments
        """
        args = args.strip().split(' ')
        return args


if __name__ == '__main__':
    HBNBCommand().cmdloop()
