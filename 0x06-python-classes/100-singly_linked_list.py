
#!/usr/bin/python3

"""Create a class"""


class Node:
    def __init__(self, data, next_node=None):
        """Initialize a Node with data and an optional next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method for data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method for data attribute"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter method for next_node attribute"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method for next_node attribute"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        """Initialize an empty singly linked list with a head node"""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node into the sorted position in the list"""
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Return a string representation of the singly linked list"""
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
