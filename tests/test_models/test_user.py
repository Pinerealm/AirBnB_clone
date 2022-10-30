#!/usr/bin/python3
"""This module tests the User class"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Defines tests for the User Class"""

    def test_init(self):
        """Tests the initialization of the User class"""
        u = User()
        self.assertIsInstance(u, User)
        self.assertTrue(hasattr(u, "email"))
        self.assertTrue(hasattr(u, "password"))
        self.assertTrue(hasattr(u, "first_name"))
        self.assertTrue(hasattr(u, "last_name"))

        self.assertTrue(hasattr(u, "id"))
        self.assertTrue(hasattr(u, "created_at"))
        self.assertTrue(hasattr(u, "updated_at"))

    def test_str(self):
        """Tests the __str__ method"""
        u = User()
        string = "[{}] ({}) {}".format(u.__class__.__name__, u.id,
                                       u.__dict__)
        self.assertEqual(string, str(u))


if __name__ == '__main__':
        unittest.main()
