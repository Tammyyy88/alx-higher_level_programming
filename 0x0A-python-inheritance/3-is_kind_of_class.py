#!/usr/bin/python3
"""Defines a class and inherited class-checking function"""

def is_kind_of_class(obj, a_class):
    """Returns True if object is instance of or if object is instance of class"""
    if isinstance(obj, a_class):
        return True
    elif issubclass(type(obj), a_class):
        return True
    else:
        return False
