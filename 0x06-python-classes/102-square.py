#!/usr/bin/python3

"""Create a class"""


class Square:
    def __init__(self, size=0):
        """Initialize a square with a given size"""
        self.size = size

    @property
    def size(self):
        """Getter method for size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size attribute"""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square"""
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparator based on square area"""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """Inequality comparator based on square area"""
        return not self.__eq__(other)

    def __gt__(self, other):
        """Greater than comparator based on square area"""
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """Greater than or equal comparator based on square area"""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False

    def __lt__(self, other):
        """Less than comparator based on square area"""
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """Less than or equal comparator based on square area"""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False
