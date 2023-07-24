#!/usr/bin/python3
"""The city module
"""
from .base_model import BaseModel


class City(BaseModel):
    """Defines the City class, inherits from BaseModel

    Attributes:
        state_id (str): The state id
        name (str): The city name
    """
    state_id = ""
    name = ""
