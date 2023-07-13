#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """Returns True if object is instance of or if object is instance of class
that inherited from, the specified class; otherwise False"""
    return isinstance(obj, a_class)
