#!/usr/bin/python3
"""Defines the HBNB console"""
import cmd

from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Defines the command intepreter"""
    prompt = "(hbnb)"

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
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            _obj = BaseModel()
            print(_obj.id)


if __name__ == '__main__':
        HBNBCommand().cmdloop()
