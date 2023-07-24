#!/usr/bin/python3
"""
This script defines a function for integer addition.
"""


def add_integer(a, b=98):
    """
    This function returns the integer addition of a and b.

    If either a or b is a non-integer and non-float, TypeError is raised.
    Float arguments are typecasted.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
