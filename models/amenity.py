#!/usr/bin/python3
"""The amenity module"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """Defines the Amenity class, inherits from BaseModel

    Attributes:
        name (str): The name of the amenity
    """
    name = ""
