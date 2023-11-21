#!/usr/bin/python3
# 2-square.py
"""Square class defination."""


class Square:
    """Square class body"""

    def __init__(slf, size=0):
        """Square class contructor
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        slf.__size = size
