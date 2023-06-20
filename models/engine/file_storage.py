#!/usr/bin/python3
"""The FileStorage module"""
import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes from a JSON file
    to instances

    Attributes:
        __file_path (str): The path to the JSON file
        __objects (dict): A dictionary of instantiated objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the '__objects' dictionary
        """
        return self.__objects

    def new(self, obj):
        """Adds an object to the '__objects' dictionary

        Args:
            obj: The object to store
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes '__objects' to the JSON file specified by '__file_path'
        """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes from the JSON file specified by '__file_path' to
        the '__objects' dictionary, if the file exists
        """
        from models.amenity import Amenity
        from models.base_model import BaseModel
        from models.city import City

        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        try:
            with open(self.__file_path, encoding="utf-8") as f:
                new_dict = json.load(f)
            for key, value in new_dict.items():
                cls = eval(value["__class__"])
                self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
