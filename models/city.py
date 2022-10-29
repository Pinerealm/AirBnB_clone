#!/usr/bin/python3
"""This is the city module"""
from .base_model import BaseModel


class City(BaseModel):
    """This is the City class"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Runs on initialization"""
        super().__init__(*args, **kwargs)
