#!/usr/bin/python3

"""Defines a node of a singly linked list"""


class Node:
    """Defines a node of a singly linked list"""

    def __init__(self, data=0, next_node=None):
        """Initializes the Node"""
        if not isinstance(data, int):
            raise TypeError("data must be an integer")

        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Returns the data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets data for the  node"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Returns the address of the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets value for  the next node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""Creates a Singly Linked List class"""


class SinglyLinkedList:
    """Creates a Singly Linked List class"""

    def __init__(self):
        """Initializes class Singly linked list."""
        self.__head = None

    def __str__(self):
        """Prints str representation of single linked list."""
        holder = self.__head
        out = ''
        while holder:
            out += str(holder.data)
            out += '\n'
            holder = holder.next_node
        return out.rstrip()

    def sorted_insert(self, value):
        """Insert in a sorted order"""
        self.__head = self._insert_recursive(self.__head, value)

    def _insert_recursive(self, current, value):
        if current is None or current.data > value:
            new_node = Node(value, current)
            return new_node
        current.next_node = self._insert_recursive(current.next_node, value)
        return current
