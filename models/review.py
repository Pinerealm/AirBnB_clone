#!/usr/bin/python3
"""This is the review module"""
from .base_model import BaseModel


class Review(BaseModel):
    """This is the Review class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Runs on initialization"""
        super().__init__(*args, **kwargs)
