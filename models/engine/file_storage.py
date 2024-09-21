#!/usr/bin/python3
"""
This module defines a FileStorage class that stores
and retrieves objects to and from a JSON file.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    A file storage system for storing and retrieving objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of all objects currently stored.

        Returns:
            dict: A dictionary of all objects currently stored.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.

        Args:
            obj (object): The object to be added to the storage.
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        Saves the objects in the storage to a JSON file.
        """
        obj_dict = {}

        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()

        try:
            with open(self.__file_path, 'w') as file:
                json.dump(obj_dict, file, indent=2)
        except FileNotFoundError:
            pass

    def reload(self):
        """
        Reloads the objects from the JSON file into the storage.
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)

                for key, value in obj_dict.items():
                    self.__objects[key] = eval(
                        f"{value['__class__']}(**{value})")

        except FileNotFoundError:
            pass
