#!/usr/bin/env python3
# base_model.py
"""Module contains BaseModel class that povides a template for
subclasses
"""
import datetime


class BaseModel:
    """Defines all common attributes/methods for subclasses
    """
    # Todo: implement __init__ method with attributes
    #   id, created_at, and updated_at

    # Todo: Add __str__ magic method

    # Todo: Add public instance method `save(self)`
    def save(self):
        """
        Save object
        """
        self.updated_at = datetime.datetime.now()

    # Todo: Add public instance method `to_dict(self)`
    def to_dict(self):
        """
        Returns a dictionary containing instance attributes
        and class name
        """
        _dict = self.__dict__
        _dict["__class__"] = self.__class__.__name__
        _dict["created_at"] = datetime.datetime.isoformat(self.created_at)
        _dict["updated_at"] = datetime.datetime.isoformat(self.updated_at)
        return _dict
