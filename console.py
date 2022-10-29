#!/usr/bin/python3
"""This is the entry point of the command interpreter for AirBnB_clone"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """This defines the command interpreter for AirBnB_clone"""
    prompt = '(hbnb) '
    classes = {"BaseModel": BaseModel, "User": User}

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
