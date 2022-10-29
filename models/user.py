#!/usr/bin/python3
"""This module contains the User class"""
from .base_model import BaseModel


class User(BaseModel):
    """This class defines the attributes of a user,
    inheriting from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Runs on initialization"""
        super().__init__(*args, **kwargs)
