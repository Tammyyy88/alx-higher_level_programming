#!/usr/bin/python3

def inherits_from(obj, a_class):
    """Returns True if the object is instance of class that inherited
    from specified class; otherwise False"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
