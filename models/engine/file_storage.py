#!/usr/bin/python3
"""This module contains the FileStorage class"""
import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes
    back to an instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the __objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds an object to the __objects dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        from ..base_model import BaseModel
        from ..user import User

        try:
            with open(FileStorage.__file_path, 'r') as f:
                new_dict = json.load(f)
                for key, value in new_dict.items():
                    if value['__class__'] == 'BaseModel':
                        FileStorage.__objects[key] = BaseModel(**value)
                    elif value['__class__'] == 'User':
                        FileStorage.__objects[key] = User(**value)
        except FileNotFoundError:
            pass
