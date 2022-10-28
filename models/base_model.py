#!/usr/bin/python3
"""Module contains BaseModel class that povides a template for
subclasses
"""
from uuid import uuid4
from datetime import datetime

import models


class BaseModel:
    """Defines all common attributes/methods for subclasses
    """

    def __init__(self, *args, **kwargs):
        """Initializes instance variables."""
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now()
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, k, v)
        else:
            models.storage.new(self)

    def save(self):
        """
        Save object
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing instance attributes
        and class name
        """
        _dict = self.__dict__.copy()
        _dict["__class__"] = self.__class__.__name__
        _dict["created_at"] = self.created_at.isoformat()
        _dict["updated_at"] = self.updated_at.isoformat()
        return _dict

    def __str__(self):
        """Returns the string representation of the BaseModel Instance"""
        d = self.__dict__
        return "[{}] ({}) {}".format(type(self).__name__, self.id, d)
