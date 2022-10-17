#!/usr/bin/python3
import sys


class Square:
    """Represents a Square"""

    def __init__(self, size=0):
        """ Initiates a square
        Args:
            size(int): size of square
            """
        self.__size = size

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

    def area(self):
        """ finds the areas of a square
        Returns:
            current square area
        """
        area_square = self.__size ** 2
        return area_square

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
