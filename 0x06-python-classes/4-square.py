#!/usr/bin/python3
"""Square class defination"""


class Square:
    """Square class body"""

    def __init__(slf, size=0):
        """Square contructor.
        Args:
            size (int): The size of the new square.
        """
        slf.size = size

    @property
    def size(slf):
        """return new size of the square."""
        return (slf.__size)

    @size.setter
    def size(slf, valu):
        if not isinstance(valu, int):
            raise TypeError("size must be an integer")
        elif valu < 0:
            raise ValueError("size must be >= 0")
        slf.__size = valu

    def area(slf):
        """Return area of the square."""
        return (slf.__size * slf.__size)
