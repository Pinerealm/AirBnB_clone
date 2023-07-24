#!/usr/bin/python3
"""The review module
"""
from .base_model import BaseModel


class Review(BaseModel):
    """Defines the Review class, inherits from BaseModel
    
    Attributes:
        place_id (str): The place id
        user_id (str): The user id
        text (str): The review text
    """
    place_id = ""
    user_id = ""
    text = ""
