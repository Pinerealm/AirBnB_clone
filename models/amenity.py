#!/usr/bin/python3
"""This is the amenity module"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """This is the Amenity class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Runs on initialization"""
        super().__init__(*args, **kwargs)
