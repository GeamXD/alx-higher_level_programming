#!/usr/bin/python3
import sys


class Square:
    """Represents a Square"""

    def __init__(self, size=0, position=(0, 0)):
        """ Initiates a square
        Args:
            size(int): size of square
            """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """str: initiates the property of size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """str: helps to retrieve the position"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ finds the areas of a square
        Returns:
            current square area
        """
        area_square = self.__size ** 2
        return area_square

    def my_print(self):
        if self.__size == 0 and self.__position[1] > 0:
            print("")
        else:
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    def __str__(self):
        return str(self.my_print())
