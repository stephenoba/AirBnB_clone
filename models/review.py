#!/usr/bin/env python3
"""Module contains Review class definition
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review model
    """
    place_id = ""
    user_id = ""
    text = ""
