#!/usr/bin/python3
"""Module for add_integer method."""


def add_integer(x, y=98):
    """Adds two integers.

    Args:
        x: first integer.
        y: second integer, default 98.

    Raises:
        TypeError: if x, y are not int, float.

    Returns:
        The sum of the two integers.
    """

    if type(x) not in (int, float):
        raise TypeError('x must be an integer')
    if type(y) not in (int, float):
        raise TypeError('y must be an integer')
    return int(x) + int(y)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
