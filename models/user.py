#!/usr/bin/env python3
"""Module contains class for User model
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User model
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
