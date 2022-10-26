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

    def __str__(self):
        """Returns the string representation of the BaseModel Instance"""
        d = self.__dict__
        return "[{}] ({}) {}".format(type(self).__name__, self.id, d)

