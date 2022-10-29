#!/usr/bin/python3
"""This is the user module"""
from .base_model import BaseModel


class State(BaseModel):
    """This is the State class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Runs on initialization"""
        super().__init__(*args, **kwargs)
