#!/usr/bin/python3
"""Square class defination."""


class Square:
    """Square class body"""

    def __init__(slf, size=0, position=(0, 0)):
        """Square constructor.
        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        slf.size = size
        slf.position = position

    @property
    def size(slf):
        """Getter and Setter of  the current size of the square."""
        return (slf.__size)

    @size.setter
    def size(slf, valu):
        if not isinstance(valu, int):
            raise TypeError("size must be an integer")
        elif valu < 0:
            raise ValueError("size must be >= 0")
        slf.__size = valu

    @property
    def position(slf):
        """Gett5er and Setter of  the current position of the square."""
        return (slf.__position)

    @position.setter
    def position(slf, valu):
        if (not isinstance(valu, tuple) or
                len(valu) != 2 or
                not all(isinstance(nm, int) for nm in valu) or
                not all(nm >= 0 for nm in valu)):
            raise TypeError("position must be a tuple of 2 positive integers")
        slf.__position = valu

    def area(slf):
        """Return the current area of the square."""
        return (slf.__size * slf.__size)

    def my_print(slf):
        """Print the square with the # character."""
        if slf.__size == 0:
            print("")
            return

        [print("") for l in range(0, slf.__position[1])]
        for l in range(0, slf.__size):
            [print(" ", end="") for u in range(0, slf.__position[0])]
            [print("#", end="") for h in range(0, slf.__size)]
            print("")

    def __str__(slf):
        """Define the print() representation of a Square."""
        if slf.__size != 0:
            [print("") for l in range(0, slf.__position[1])]
        for l in range(0, slf.__size):
            [print(" ", end="") for u in range(0, slf.__position[0])]
            [print("#", end="") for h in range(0, slf.__size)]
            if l != slf.__size - 1:
                print("")
        return ("")
