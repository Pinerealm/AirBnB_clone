#!/usr/bin/python3
"""Tests the console module"""
from console import HBNBCommand
from io import StringIO
from models import storage
import os
import unittest

from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """Test the console module
    """
    def setUp(self):
        """Set up for the following test methods
        """
        self.console = HBNBCommand()
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """Remove the temporary file (file.json)
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_prompt(self):
        """Test the prompt
        """
        self.assertEqual("(hbnb) ", self.console.prompt)

    def test_emptyline(self):
        """Test an empty line input
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("\n")
            self.assertEqual("", f.getvalue())

    def test_quit(self):
        """Test the quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("quit")
            self.assertEqual("", f.getvalue())

    def test_EOF(self):
        """Test the EOF command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("EOF")
            self.assertEqual("\n", f.getvalue())

    def test_create(self):
        """Test the create command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertEqual(36, len(f.getvalue().strip()))
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            self.assertEqual(36, len(f.getvalue().strip()))

    def test_show(self):
        """Test the show command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel 123456-abcdef-123456")
            self.assertEqual("** no instance found **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            key = "BaseModel." + f.getvalue().strip()
            self.console.onecmd("show BaseModel " + f.getvalue().strip())
            self.assertIn(str(storage.all()[key]) + "\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            key = "User." + f.getvalue().strip()
            self.console.onecmd("show User " + f.getvalue().strip())
            self.assertIn(str(storage.all()[key]) + "\n", f.getvalue())

    def test_destroy(self):
        """Test the destroy command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel 123456-abcdef-123456")
            self.assertEqual("** no instance found **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            key = "BaseModel." + f.getvalue().strip()
            self.console.onecmd("destroy BaseModel " + f.getvalue().strip())
            self.assertNotIn(key, storage.all())

    def test_all(self):
        """Test the all command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        # Test the all command with no objects
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            self.assertEqual("[]\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
            self.console.onecmd("create Place")
            self.console.onecmd("all BaseModel")

            self.assertIn("BaseModel", f.getvalue())
            self.assertNotIn("User", f.getvalue())
            self.assertNotIn("Place", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
            self.console.onecmd("create Place")
            self.console.onecmd("all User")

            self.assertNotIn("BaseModel", f.getvalue())
            self.assertIn("User", f.getvalue())
            self.assertNotIn("Place", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
            self.console.onecmd("create Place")
            self.console.onecmd("all")

            self.assertIn("BaseModel", f.getvalue())
            self.assertIn("User", f.getvalue())
            self.assertIn("Place", f.getvalue())

    def test_update(self):
        """Test the update command
        """
        object_id = ""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel 123456-abcdef-123456")
            self.assertEqual("** no instance found **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            object_id = f.getvalue().strip()
            self.console.onecmd("update BaseModel " + object_id)
            self.assertIn("** attribute name missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel " + object_id +
                                " first_name")
            self.assertEqual("** value missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel " + object_id +
                                " first_name \"Betty\"")
            self.assertEqual("", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel " + object_id)
            self.assertIn("Betty", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel " + object_id +
                                " first_name \"Holberton\"")
            self.assertEqual("", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel " + object_id)
            self.assertIn("Holberton", f.getvalue())
