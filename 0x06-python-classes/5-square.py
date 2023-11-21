#!/usr/bin/python3
"""Square class defination"""


class Square:
    """Square class body"""

    def __init__(slf, size):
        """Square contructor
        Args:
            size (int): The size of the new square.
        """
        slf.size = size

    @property
    def size(slf):
        """Square setter and getter for __size."""
        return (slf.__size)

    @size.setter
    def size(slf, valu):
        if not isinstance(valu, int):
            raise TypeError("size must be an integer")
        elif valu < 0:
            raise ValueError("size must be >= 0")
        slf.__size = valu

    def area(slf):
        """Return th area of a square."""
        return (slf.__size * slf.__size)

    def my_print(slf):
        """Print stdout the square with the character"""
        for l in range(0, slf.__size):
            [print("#", end="") for k in range(slf.__size)]
            print("")
        if slf.__size == 0:
            print("")
