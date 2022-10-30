#!/usr/bin/python3
"""This module tests the FileStorage class"""
import unittest
from models.engine.file_storage import FileStorage
import models


class TestFileStorage(unittest.TestCase):
    """Defines tests for the FileStorage Class"""

    def test_init(self):
        """Tests the initialization of the FileStorage class"""
        fs = FileStorage()
        self.assertIsInstance(fs, FileStorage)
        self.assertTrue(hasattr(fs, "_FileStorage__file_path"))
        self.assertTrue(hasattr(fs, "_FileStorage__objects"))

    def test_all(self):
        """Tests the all method"""
        fs = FileStorage()
        self.assertIsInstance(fs.all(), dict)

    def test_new(self):
        """Tests the new method"""
        fs = FileStorage()
        bm = models.base_model.BaseModel()
        fs.new(bm)
        key = "{}.{}".format(bm.__class__.__name__, bm.id)
        self.assertTrue(key in fs.all())

    def test_save(self):
        """Tests the save method"""
        fs = FileStorage()
        bm = models.base_model.BaseModel()
        fs.new(bm)
        fs.save()
        key = "{}.{}".format(bm.__class__.__name__, bm.id)
        with open(fs._FileStorage__file_path, "r") as f:
            self.assertTrue(key in f.read())

    def test_reload(self):
        """Tests the reload method"""
        fs = FileStorage()
        bm = models.base_model.BaseModel()
        fs.new(bm)
        fs.save()
        fs.reload()
        key = "{}.{}".format(bm.__class__.__name__, bm.id)
        self.assertTrue(key in fs.all())

if __name__ == '__main__':
        unittest.main()
