#!/usr/bin/python3
"""Square class defination."""


class Square:
    """Square class body."""

    def __init__(slf, size=0):
        """Square contructor.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        slf.__size = size

    def area(slf):
        """Return the new area of the square."""
        return (slf.__size * slf.__size)
