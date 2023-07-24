#!/usr/bin/python3
"""Instantiates a FileStorage object
"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
