#!/usr/bin/python3
"""Module contains BaseModel class that povides a template for
subclasses
"""
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Defines all common attributes/methods for subclasses
    """

    def __init__(self):
        """Initializes instance variables."""
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now()

    def save(self):
        """
        Save object
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing instance attributes
        and class name
        """
        _dict = self.__dict__
        _dict["__class__"] = self.__class__.__name__
        _dict["created_at"] = datetime.isoformat(self.created_at)
        _dict["updated_at"] = datetime.isoformat(self.updated_at)
        return _dict

    def __str__(self):
        """Returns the string representation of the BaseModel Instance"""
        d = self.__dict__
        return "[{}] ({}) {}".format(type(self).__name__, self.id, d)
