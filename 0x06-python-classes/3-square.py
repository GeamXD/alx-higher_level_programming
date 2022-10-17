#!/usr/bin/python3
class Square:
    """Represents a Square"""

    def __init__(self, size=0):
        """ Initiates a square
        Args:
            size(int): size of square
            """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ finds the areas of a square
        Returns:
            current square area
        """
        area_square = self.__size ** 2
        return area_square
