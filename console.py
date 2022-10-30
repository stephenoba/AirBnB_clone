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

    def do_show(self,arg):
        """
        Prints the string representation of an instance
        based on the class name and id

        Usage: |
            show <class name> <id>
        """
        if arg:
            objects = models.storage.all()
            try:
                args = self.clean_args(arg)
                cls_name = args[0]
                _id = args[1]
                obj_list = list(filter(lambda x: x.id == _id,
                    objects.values()))
                print(str(obj_list[0]))
            except IndexError:
                print("** instance id missing **")
            except KeyError:
                print("** no instance found **")
        else:
            print("** class name missing **")

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
            args = self.clean_args(arg)
            objects = dict(filter(lambda x: isinstance(x[1], eval(args[0])),
                    objects.items()))
        print(list(map(lambda x: str(x), objects.values())))

    def do_update(self, arg):
        """
        Updates an instance based on the class name an id

        Usage: |
            update <class name> <id> <attribute name> "<attribute value>"
        """
        if not arg:
            print("** class name missing **")
            return

        args = self.clean_args(arg)
        if len(args) == 3:
            print("** value missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return


    @staticmethod
    def clean_args(args: str):
        """
        clean arguments
        """
        args = args.strip().split(' ')
        return args


if __name__ == '__main__':
    HBNBCommand().cmdloop()
