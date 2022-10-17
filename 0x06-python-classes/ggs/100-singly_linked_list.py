#!/usr/bin/python3
class Node:
    """ Singly linked list"""

    def __init__(self, data, next_node=None):
        """ initializes Node

        Args:
            data(int): data of node
            next_node(node) = pointers to next node
        Returns:
            A pointer to next node
        """

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ retrieves data"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ retrieves next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) or value is None:
            raise TypeError("next_node must be a Node Object")


class SinglyLinkedList(Node):
    """represents a single linked list"""

    def __init__(self, data):
        super().__init__(data)
        self.__head = data

    def __str__(self):
        return str(self.__head)

