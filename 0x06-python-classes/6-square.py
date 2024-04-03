
#!/usr/bin/python3
"""Create class"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with a given size and position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method for size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method for position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for position attribute"""
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(i, int) for i in value) or \
           not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with '#' characters and respect the position"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
