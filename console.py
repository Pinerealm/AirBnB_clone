#!/usr/bin/python3
"""This is the entry point of the command interpreter for AirBnB_clone"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models import storage


class HBNBCommand(cmd.Cmd):
    """This defines the command interpreter for AirBnB_clone"""
    prompt = '(hbnb) '
    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}

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

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        if not line:
            print("** class name missing **")
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.classes[line]()
            print(new_instance.id)
            new_instance.save()

    def do_show(self, line):
        """Prints the string representation of an instance based on
        the class name and id"""
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """Prints the string representation of all instances or the specified
        class name"""
        args = line.split()
        if not line:
            print([str(v) for k, v in storage.all().items()])
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(v) for k, v in storage.all().items() if args[0] in k])

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or
        updating attribute"""
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                if args[3][0] == '"' and args[3][-1] == '"':
                    args[3] = args[3][1:-1]
                if args[3].isdigit():
                    if '.' in args[3]:
                        args[3] = float(args[3])
                    else:
                        args[3] = int(args[3])
                setattr(storage.all()[key], args[2], args[3])
                storage.all()[key].save()

    def do_help(self, line):
        """Prints help messages for commands"""
        commands = {'EOF': self.do_EOF.__doc__,
                    'quit': self.do_quit.__doc__,
                    'create': self.do_create.__doc__,
                    'show': self.do_show.__doc__,
                    'destroy': self.do_destroy.__doc__,
                    'all': self.do_all.__doc__,
                    'update': self.do_update.__doc__}
        if line in commands:
            print(commands[line])
        else:
            super().do_help(line)

    def default(self, line: str):
        """Handles other previously undefined commands"""
        methods = {'show': self.do_show, 'destroy': self.do_destroy,
                   'update': self.do_update}
        args = line.split('.')

        if len(args) != 2:
            super().default(line)
        elif args[0] not in self.classes:
            print("** class doesn't exist **")

        elif args[1] == 'all()':
            self.do_all(args[0])
        elif args[1] == 'count()':
            print(len([v for k, v in storage.all().items() if args[0] in k]))
        
        key = args[1].split('(')[0]
        if key in methods:
            id = args[1].split('"')[1]
            if key == 'update':
                attr = args[1].split('"')[3]
                value = args[1].split('"')[5]
                methods[key](f'{args[0]} {id} {attr} {value}')
            methods[key](f'{args[0]} {id}')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
