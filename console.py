#!/usr/bin/python3
"""The console/command interpreter for the AirBnB_clone project
"""
import ast
import cmd
from models import storage
from models.amenity import Amenity

from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review

from models.state import State
from models.user import User
import sys


class HBNBCommand(cmd.Cmd):
    """Defines the HBNBCommand class for AirBnB_clone
    """
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''
    classes = ('BaseModel', 'User', 'State', 'Review',
               'City', 'Amenity', 'Place')

    def preloop(self):
        """Displays an entry prompt on non-interactive mode
        """
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def postloop(self):
        """Displays an exit prompt on non-interactive mode
        """
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def parseline(self, line):
        """Parses the line before it is executed
        """
        if '(' in line:
            line = line.replace('.', ' ', 1).replace('(', ' ', 1)
            line = line.replace(')', '')
            if '{' in line and ': ' in line and '}' in line:
                #  Update if dictionary is given
                line = line.replace(': ', '##').replace(', ', '%%')
                line = line.replace('%%{', ' {', 1)
                line = line.split(" ", 3)
                line[3] = line[3].replace('##', ': ').replace('%%', ', ')
                line[2] = line[2].replace('"', '').replace(',', '')
                line = " *".join([line[1], line[0], line[2], line[3]])
                return super().parseline(line)
            line = line.split()
            if len(line) == 3:
                #  For show and destroy
                line[2] = line[2].replace('"', '')
                line = " ".join([line[1], line[0], line[2]])
            elif len(line) >= 5:
                #  Update if attribute name and value are given
                line[2] = line[2].replace('"', '')
                line[2] = line[2].replace(',', '')
                line[3] = line[3].replace('"', '')
                line[3] = line[3].replace(',', '')
                line[4] = line[4].replace('"', '')
                line = " ".join([line[1], line[0], line[2], line[3], line[4]])
            else:
                line = " ".join([line[1], line[0]])

        return super().parseline(line)

    def do_quit(self, arg):
        """Exit the program with the command 'quit'
        """
        return True

    def do_EOF(self, arg):
        """Exit the program on receiving the EOF signal
        """
        print()
        return True

    def emptyline(self):
        """Does nothing when an empty line is entered
        """
        return False

    def do_create(self, arg):
        """Creates a new instance of a given class, saves it to a JSON file,
        and prints the id

        Usage: create <class name>, OR <class name>.create()
        """
        if not arg:
            print("** class name missing **")
            return
        tokens = arg.split()
        if tokens[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(tokens[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the
        class name and id

        Usage: show <class name> <id> OR <class name>.show(<id>)
        """
        if not arg:
            print("** class name missing **")
            return
        tokens = arg.split()
        if tokens[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(tokens) == 1:
            print("** instance id missing **")

        else:
            key = tokens[0] + '.' + tokens[1]
            if key not in storage.all():
                print('** no instance found **')
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id

        Usage: destroy <class name> <id> OR <class name>.destroy(<id>)
        """
        if not arg:
            print("** class name missing **")
            return
        tokens = arg.split()
        if tokens[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(tokens) == 1:
            print("** instance id missing **")

        else:
            key = tokens[0] + '.' + tokens[1]
            if key not in storage.all():
                print('** no instance found **')
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """Displays the string representation of all instances or
        all instances of a class

        Usage: all <class name> OR <class name>.all() OR all
        """
        output = []
        if not arg:
            for value in storage.all().values():
                output.append(str(value))
            print(output)

        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                if arg == key.split('.')[0]:
                    output.append(str(value))
            print(output)

    def do_update(self, arg):
        """Updates/adds to an instance's attributes

        Usage: update <class name> <id> <attribute name> "<attribute value>"
            OR <class name>.update(<id>, <attribute name>, "<attribute value>)"
            OR <class name>.update(<id>, <dictionary representation>)
        """
        if not arg:
            print("** class name missing **")
            return
        if '*' in arg:
            tokens = arg.split(' *')
            tokens[0] = tokens[0].replace('*', '', 1)
            tokens[2] = ast.literal_eval(tokens[2])
        else:
            tokens = arg.split(" ", 4)

        if tokens[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(tokens) == 1:
            print("** instance id missing **")
            return

        obj_dict = storage.all()
        key = f"{tokens[0]}.{tokens[1]}"
        if key not in obj_dict:
            print("** no instance found **")
            return

        if len(tokens) == 2:
            print("** attribute name missing **")
        elif len(tokens) == 3:
            if type(tokens[2]) is dict:
                for k, v in tokens[2].items():
                    setattr(storage.all()[key], k, v)
                    storage.save()
                return
            print("** value missing **")

        else:
            if tokens[3][0] == tokens[3][-1] == '"':
                tokens[3] = tokens[3][1:-1]
            if tokens[3].isdigit():
                tokens[3] = int(tokens[3])
            if tokens[3].replace('.', "", 1).isdigit():
                tokens[3] = float(tokens[3])

            setattr(storage.all()[key], tokens[2], tokens[3])
            storage.save()

    def default(self, line):
        """Parse lines which are not recognized as commands
        """
        tokens = line.split(' ')
        if tokens[0] == 'count':
            count = 0
            for key in storage.all():
                if tokens[1] in key:
                    count += 1
            print(count)
        else:
            return super().default(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
