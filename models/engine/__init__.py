#!/usr/bin/python3
"""Module defines all common attributes/method for other classes"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
