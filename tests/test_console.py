#!/usr/bin/python3
"""Tests the command interpreter
"""
from console import HBNBCommand
from io import StringIO
from models import storage
import os

import sys
import unittest
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """Test the console module
    """
    @classmethod
    def setUpClass(cls):
        """Sets up the class
        """
        storage._FileStorage__file_path = "test.json"

    def setUp(self):
        """Sets up each test
        """
        self.cns = HBNBCommand()
        storage._FileStorage__objects = {}
        if os.path.exists("test.json"):
            os.remove("test.json")

    @unittest.skipUnless(sys.__stdin__.isatty(), "interactive mode only")
    def test_prompt(self):
        """Test the prompt
        """
        self.assertEqual("(hbnb) ", self.cns.prompt)

    def test_help(self):
        """Test the help command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("help quit")
            output = "Exits the program\n"
            self.assertEqual(output, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("help EOF")
            output = "Exits the program on receiving the EOF signal\n"
            self.assertEqual(output, f.getvalue())

    def test_emptyline(self):
        """Test an empty line input
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("\n")
            self.assertEqual("", f.getvalue())

    def test_quit(self):
        """Test the quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("quit")
            self.assertEqual("", f.getvalue())

    def test_EOF(self):
        """Test the EOF command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("EOF")
            self.assertEqual("\n", f.getvalue())

    def test_create(self):
        """Test the create command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create BaseModel")
            self.assertEqual(36, len(f.getvalue().strip()))
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create User")
            self.assertEqual(36, len(f.getvalue().strip()))

    def test_show(self):
        """Test the show command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("show")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("show MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("show BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("show BaseModel 123456-abcdef-123456")
            self.assertEqual("** no instance found **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            key = "BaseModel." + obj_id
            self.assertIn(key, storage.all())
            self.cns.onecmd("show BaseModel " + obj_id)
            self.assertIn(str(storage.all()[key]) + "\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd('BaseModel.show("' + obj_id + '")')
            self.assertEqual(str(storage.all()[key]) + "\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create User")
            obj_id = f.getvalue().strip()
            key = "User." + obj_id
            self.assertIn(key, storage.all())
            self.cns.onecmd("show User " + obj_id)
            self.assertIn(str(storage.all()[key]) + "\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd('User.show("' + obj_id + '")')
            self.assertEqual(str(storage.all()[key]) + "\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create State")
            obj_id = f.getvalue().strip()
            key = "State." + obj_id
            self.assertIn(key, storage.all())
            self.cns.onecmd("show State " + obj_id)
            self.assertIn(str(storage.all()[key]) + "\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd('State.show("' + obj_id + '")')
            self.assertEqual(str(storage.all()[key]) + "\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create City")
            obj_id = f.getvalue().strip()
            key = "City." + obj_id
            self.assertIn(key, storage.all())
            self.cns.onecmd("show City " + obj_id)
            self.assertIn(str(storage.all()[key]) + "\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd('City.show("' + obj_id + '")')
            self.assertEqual(str(storage.all()[key]) + "\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create Amenity")
            obj_id = f.getvalue().strip()
            key = "Amenity." + obj_id
            self.assertIn(key, storage.all())
            self.cns.onecmd("show Amenity " + obj_id)
            self.assertIn(str(storage.all()[key]) + "\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd('Amenity.show("' + obj_id + '")')
            self.assertEqual(str(storage.all()[key]) + "\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create Place")
            obj_id = f.getvalue().strip()
            key = "Place." + obj_id
            self.assertIn(key, storage.all())
            self.cns.onecmd("show Place " + obj_id)
            self.assertIn(str(storage.all()[key]) + "\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd('Place.show("' + obj_id + '")')
            self.assertEqual(str(storage.all()[key]) + "\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create Review")
            obj_id = f.getvalue().strip()
            key = "Review." + obj_id
            self.assertIn(key, storage.all())
            self.cns.onecmd("show Review " + obj_id)
            self.assertIn(str(storage.all()[key]) + "\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd('Review.show("' + obj_id + '")')
            self.assertEqual(str(storage.all()[key]) + "\n", f.getvalue())

    def test_destroy(self):
        """Test the destroy command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("destroy")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("destroy MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("destroy BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("destroy BaseModel 123456-abcdef-123456")
            self.assertEqual("** no instance found **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create BaseModel")
            self.cns.onecmd("create BaseModel")
            obj_id1, obj_id2 = f.getvalue().strip().split('\n')
            key = "BaseModel." + obj_id1
            self.assertIn(key, storage.all())
            self.cns.onecmd("destroy BaseModel " + obj_id1)
            self.assertNotIn(key, storage.all())

            key = "BaseModel." + obj_id2
            self.assertIn(key, storage.all())
            self.cns.onecmd('BaseModel.destroy("' + obj_id2 + '")')
            self.assertNotIn(key, storage.all())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create User")
            self.cns.onecmd("create User")
            obj_id1, obj_id2 = f.getvalue().strip().split('\n')
            key = "User." + obj_id1
            self.assertIn(key, storage.all())
            self.cns.onecmd("destroy User " + obj_id1)
            self.assertNotIn(key, storage.all())

            key = "User." + obj_id2
            self.assertIn(key, storage.all())
            self.cns.onecmd('User.destroy("' + obj_id2 + '")')
            self.assertNotIn(key, storage.all())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create State")
            self.cns.onecmd("create State")
            obj_id1, obj_id2 = f.getvalue().strip().split('\n')
            key = "State." + obj_id1
            self.assertIn(key, storage.all())
            self.cns.onecmd("destroy State " + obj_id1)
            self.assertNotIn(key, storage.all())

            key = "State." + obj_id2
            self.assertIn(key, storage.all())
            self.cns.onecmd('State.destroy("' + obj_id2 + '")')
            self.assertNotIn(key, storage.all())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create City")
            self.cns.onecmd("create City")
            obj_id1, obj_id2 = f.getvalue().strip().split('\n')
            key = "City." + obj_id1
            self.assertIn(key, storage.all())
            self.cns.onecmd("destroy City " + obj_id1)
            self.assertNotIn(key, storage.all())

            key = "City." + obj_id2
            self.assertIn(key, storage.all())
            self.cns.onecmd('City.destroy("' + obj_id2 + '")')
            self.assertNotIn(key, storage.all())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create Amenity")
            self.cns.onecmd("create Amenity")
            obj_id1, obj_id2 = f.getvalue().strip().split('\n')
            key = "Amenity." + obj_id1
            self.assertIn(key, storage.all())
            self.cns.onecmd("destroy Amenity " + obj_id1)
            self.assertNotIn(key, storage.all())

            key = "Amenity." + obj_id2
            self.assertIn(key, storage.all())
            self.cns.onecmd('Amenity.destroy("' + obj_id2 + '")')
            self.assertNotIn(key, storage.all())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create Place")
            self.cns.onecmd("create Place")
            obj_id1, obj_id2 = f.getvalue().strip().split('\n')
            key = "Place." + obj_id1
            self.assertIn(key, storage.all())
            self.cns.onecmd("destroy Place " + obj_id1)
            self.assertNotIn(key, storage.all())

            key = "Place." + obj_id2
            self.assertIn(key, storage.all())
            self.cns.onecmd('Place.destroy("' + obj_id2 + '")')
            self.assertNotIn(key, storage.all())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create Review")
            self.cns.onecmd("create Review")
            obj_id1, obj_id2 = f.getvalue().strip().split('\n')
            key = "Review." + obj_id1
            self.assertIn(key, storage.all())
            self.cns.onecmd("destroy Review " + obj_id1)
            self.assertNotIn(key, storage.all())

            key = "Review." + obj_id2
            self.assertIn(key, storage.all())
            self.cns.onecmd('Review.destroy("' + obj_id2 + '")')
            self.assertNotIn(key, storage.all())

    def test_all(self):
        """Test the all command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("all MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        # Test the all command with no objects
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("all")
            self.assertEqual("[]\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create BaseModel")
            self.cns.onecmd("create User")
            self.cns.onecmd("create Place")
            self.cns.onecmd("all BaseModel")

            self.assertIn("BaseModel", f.getvalue())
            self.assertNotIn("User", f.getvalue())
            self.assertNotIn("Place", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd('BaseModel.all()')
            self.assertIn("BaseModel", f.getvalue())
            self.assertNotIn("User", f.getvalue())
            self.assertNotIn("Place", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create BaseModel")
            self.cns.onecmd("create User")
            self.cns.onecmd("create Place")
            self.cns.onecmd("all User")

            self.assertNotIn("BaseModel", f.getvalue())
            self.assertIn("User", f.getvalue())
            self.assertNotIn("Place", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd('User.all()')
            self.assertNotIn("BaseModel", f.getvalue())
            self.assertIn("User", f.getvalue())
            self.assertNotIn("Place", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create Review")
            self.cns.onecmd("create State")
            self.cns.onecmd("create City")
            self.cns.onecmd("create Amenity")
            self.cns.onecmd("create Place")

            self.cns.onecmd("Review.all()")
            self.assertIn("Review", f.getvalue())
            self.cns.onecmd("State.all()")
            self.assertIn("State", f.getvalue())
            self.cns.onecmd("City.all()")

            self.assertIn("City", f.getvalue())
            self.cns.onecmd("Amenity.all()")
            self.assertIn("Amenity", f.getvalue())
            self.cns.onecmd("Place.all()")
            self.assertIn("Place", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create BaseModel")
            self.cns.onecmd("create User")
            self.cns.onecmd("create Place")
            self.cns.onecmd("all")

            self.assertIn("BaseModel", f.getvalue())
            self.assertIn("User", f.getvalue())
            self.assertIn("Place", f.getvalue())

    def test_update(self):
        """Test the update command
        """
        object_id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("update")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("update MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("update BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("update BaseModel 123456-abcdef-123456")
            self.assertEqual("** no instance found **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create BaseModel")
            object_id = f.getvalue().strip()
            self.cns.onecmd("update BaseModel " + object_id)
            self.assertIn("** attribute name missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("update BaseModel " + object_id +
                            " first_name")
            self.assertEqual("** value missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("update BaseModel " + object_id +
                            " first_name \"Betty\"")
            self.assertEqual("", f.getvalue())
            self.cns.onecmd("show BaseModel " + object_id)
            self.assertIn("Betty", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("update BaseModel " + object_id +
                            " first_name \"Holberton\"")
            self.assertEqual("", f.getvalue())
            self.cns.onecmd("show BaseModel " + object_id)
            self.assertIn("Holberton", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd('BaseModel.update("' + object_id +
                            '", "first_name", "Zaid")')
            self.assertEqual("", f.getvalue())
            self.cns.onecmd("show BaseModel " + object_id)
            self.assertIn("Zaid", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd('BaseModel.update("' + object_id +
                            '", {"first_name": "John", "age": 89})')
            self.assertEqual("", f.getvalue())
            self.cns.onecmd("show BaseModel " + object_id)
            self.assertIn("John", f.getvalue())
            self.assertIn("89", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create User")
            object_id = f.getvalue().strip()
            self.cns.onecmd('User.update("' + object_id +
                            '", "first_name", "Mary")')
            self.cns.onecmd("show User " + object_id)
            self.assertIn("Mary", f.getvalue())

            self.cns.onecmd('User.update("' + object_id +
                            '", {"first_name": "Bob", "age": 60})')
            self.cns.onecmd("show User " + object_id)
            self.assertIn("Bob", f.getvalue())
            self.assertIn("60", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create State")
            object_id = f.getvalue().strip()
            self.cns.onecmd('State.update("' + object_id +
                            '", "name", "California")')
            self.cns.onecmd("show State " + object_id)
            self.assertIn("California", f.getvalue())

            self.cns.onecmd('State.update("' + object_id +
                            '", {"name": "Nevada"})')
            self.cns.onecmd("show State " + object_id)
            self.assertIn("Nevada", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create City")
            object_id = f.getvalue().strip()
            self.cns.onecmd('City.update("' + object_id +
                            '", "name", "San_Francisco")')
            self.cns.onecmd("show City " + object_id)
            self.assertIn("San_Francisco", f.getvalue())

            self.cns.onecmd('City.update("' + object_id +
                            '", {"name": "San_Jose"})')
            self.cns.onecmd("show City " + object_id)
            self.assertIn("San_Jose", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create Amenity")
            object_id = f.getvalue().strip()
            self.cns.onecmd('Amenity.update("' + object_id +
                            '", "name", "Wifi")')
            self.cns.onecmd("show Amenity " + object_id)
            self.assertIn("Wifi", f.getvalue())

            self.cns.onecmd('Amenity.update("' + object_id +
                            '", {"name": "Cable"})')
            self.cns.onecmd("show Amenity " + object_id)
            self.assertIn("Cable", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create Place")
            object_id = f.getvalue().strip()
            self.cns.onecmd('Place.update("' + object_id +
                            '", "name", "House")')
            self.cns.onecmd("show Place " + object_id)
            self.assertIn("House", f.getvalue())

            self.cns.onecmd('Place.update("' + object_id +
                            '", {"name": "Apartment"})')
            self.cns.onecmd("show Place " + object_id)
            self.assertIn("Apartment", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("create Review")
            object_id = f.getvalue().strip()
            self.cns.onecmd('Review.update("' + object_id +
                            '", "text", "Great")')
            self.cns.onecmd("show Review " + object_id)
            self.assertIn("Great", f.getvalue())

            self.cns.onecmd('Review.update("' + object_id +
                            '", {"text": "Good"})')
            self.cns.onecmd("show Review " + object_id)
            self.assertIn("Good", f.getvalue())

    def test_count(self):
        """Test the .count() command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("BaseModel.count()")
            self.assertEqual("0\n", f.getvalue())
            self.cns.onecmd("create BaseModel")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("BaseModel.count()")
            self.assertEqual("1\n", f.getvalue())
            self.cns.onecmd("create User")
            self.cns.onecmd("create User")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("User.count()")
            self.assertEqual("2\n", f.getvalue())
            self.cns.onecmd("create State")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("State.count()")
            self.assertEqual("1\n", f.getvalue())
            self.cns.onecmd("create Place")
            self.cns.onecmd("create Place")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("Place.count()")
            self.assertEqual("2\n", f.getvalue())
            self.cns.onecmd("create City")
            self.cns.onecmd("create City")
            self.cns.onecmd("create City")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("City.count()")
            self.assertEqual("3\n", f.getvalue())
            self.cns.onecmd("create Amenity")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("Amenity.count()")
            self.assertEqual("1\n", f.getvalue())
            self.cns.onecmd("create Review")
            self.cns.onecmd("create Review")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cns.onecmd("Review.count()")
            self.assertEqual("2\n", f.getvalue())
