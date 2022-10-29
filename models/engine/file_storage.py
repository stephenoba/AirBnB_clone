#!/usr/bin/env python3
"""Module provides class used to manage file storage
"""

import json
from models.base_model import BaseModel
import sys


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON
    files to instances
    """
    __file_path = "filestore.json"
    __objects = {}

    def all(self):
        """Returns the dictionary '_objects'"""
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in '_objects' the 'obj' with key '<obj classname>.id
        """
        clsname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(clsname, obj.id)] = obj

    def save(self):
        """
        Serializes '__objects' to the JSON file
        """
        dictn = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(dictn, f, indent=4)

    def reload(self):
        """
        Deserializes the JSON file to '__objects' if the JSON file exists
        """
        objects = {}
        try:
            with open(FileStorage.__file_path, encoding='utf8') as f:
                objects = json.load(f)
                for _, obj_dict in objects.items():
                    clsname = obj_dict.pop("__class__")
                    cls = getattr(sys.modules[__name__], clsname)
                    try:
                        self.new(cls(**obj_dict))
                    except (TypeError, ValueError):
                        # we could output to stderr
                        continue
        except FileNotFoundError:
            return
