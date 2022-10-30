#!/usr/bin/python3
"""This module tests the BaseModel class"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Defines tests for the BaseModel Class"""

    def test_init(self):
        """Tests the initialization of the BaseModel class"""
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)
        self.assertTrue(hasattr(bm, "id"))
        self.assertTrue(hasattr(bm, "created_at"))
        self.assertTrue(hasattr(bm, "updated_at"))

    def test_str(self):
        """Tests the __str__ method"""
        bm = BaseModel()
        string = "[{}] ({}) {}".format(bm.__class__.__name__, bm.id,
                                       bm.__dict__)
        self.assertEqual(string, str(bm))

    def test_save(self):
        """Tests the save method"""
        bm = BaseModel()
        bm.save()
        self.assertNotEqual(bm.created_at, bm.updated_at)

    def test_to_dict(self):
        """Tests the to_dict method"""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertIsInstance(bm_dict, dict)
        self.assertEqual(bm_dict["__class__"], "BaseModel")
        self.assertEqual(bm_dict["created_at"], bm.created_at.isoformat())
        self.assertEqual(bm_dict["updated_at"], bm.updated_at.isoformat())


if __name__ == '__main__':
        unittest.main()
