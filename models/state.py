#!/usr/bin/python3
"""The state module
"""
from .base_model import BaseModel


class State(BaseModel):
    """Defines the State class, inherits from BaseModel

    Attributes:
        name (str): The state name
    """
    name = ""
