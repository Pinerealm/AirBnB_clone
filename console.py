#!/usr/bin/python3
"""This is the entry point of the command interpreter for AirBnB_clone"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This defines the command interpreter for AirBnB_clone"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_help(self, line):
        """Prints help messages for commands"""
        if line == 'EOF':
            print(self.do_EOF.__doc__)
        elif line == 'quit':
            print(self.do_quit.__doc__)
        else:
            super().do_help(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
