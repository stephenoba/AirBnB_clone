#!/usr/bin/python3
"""Defines the HBNB console"""
import cmd

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


if __name__ == '__main__':
        HBNBCommand().cmdloop()
