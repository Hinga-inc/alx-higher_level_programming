# 0x0C. Python - Almost a circle

## General
### What is Unit testing and how to implement it in a large project
### How to serialize and deserialize a Class
### How to write and read a JSON file
### ### What is *args and how to use it
### What is **kwargs and how to use it
### How to handle named arguments in a function

## Tasks

0. If it's not tested it doesn't work
#### mandatory
#### All your files, classes and methods must be unit tested and be PEP 8 validated.

``` shell
    guillaume@ubuntu:~/$ python3 -m unittest discover tests
    ...................................................................................
    ...................................................................................
    .......................
    ----------------------------------------------------------------------
    Ran 189 tests in 13.135s

    OK
    guillaume@ubuntu:~/$
```
#### Note that this is just an example. The number of tests you create can be different from the above example.

#### Repo:

##### GitHub repository: alx-higher_level_programming
##### Directory: 0x0C-python-almost_a_circle
##### File: tests/

1. Base class
#### mandatory
#### Write the first class Base:

#### Create a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package

#### Create a file named models/base.py:

#### Class Base:
#### private class attribute __nb_objects = 0
#### class constructor: def __init__(self, id=None)::
#### if id is not None, assign the public instance attribute id with this argument value - you can assume id is an integer and you don’t need to test the type of it
#### otherwise, increment __nb_objects and assign the new value to the public instance attribute id
#### This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)

``` shell
    guillaume@ubuntu:~/$ cat 0-main.py
    #!/usr/bin/python3
    """ 0-main """
    from models.base import Base

    if __name__ == "__main__":

        b1 = Base()
        print(b1.id)

        b2 = Base()
        print(b2.id)

        b3 = Base()
        print(b3.id)

        b4 = Base(12)
        print(b4.id)

        b5 = Base()
        print(b5.id)

    guillaume@ubuntu:~/$ ./0-main.py
    1
    2
    3
    12
    4
    guillaume@ubuntu:~/$ 
```
#### Repo:

##### GitHub repository: alx-higher_level_programming
##### Directory: 0x0C-python-almost_a_circle
##### File: models/base.py, models/__init__.py

2. First Rectangle
#### mandatory
#### Write the class Rectangle that inherits from Base:

#### In the file models/rectangle.py
#### Class Rectangle inherits from Base
#### Private instance attributes, each with its own public getter and setter:
#### __width -> width
#### __height -> height
#### __x -> x
#### __y -> y
#### Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
#### Call the super class with id - this super call with use the logic of the __init__ of the Base class
#### Assign each argument width, height, x and y to the right attribute
#### Why private attributes with getter/setter? Why not directly public attribute?

#### Because we want to protect attributes of our class. With a setter, you are able to validate what a developer is trying to assign to a variable. So after, in your class you can “trust” these attributes.

``` shell
    guillaume@ubuntu:~/$ cat 1-main.py
    #!/usr/bin/python3
    """ 1-main """
    from models.rectangle import Rectangle

    if __name__ == "__main__":

        r1 = Rectangle(10, 2)
        print(r1.id)

        r2 = Rectangle(2, 10)
        print(r2.id)

        r3 = Rectangle(10, 2, 0, 0, 12)
        print(r3.id)

    guillaume@ubuntu:~/$ ./1-main.py
    1
    2
    12
guillaume@ubuntu:~/$ 
```
#### Repo:

##### GitHub repository: alx-higher_level_programming
##### Directory: 0x0C-python-almost_a_circle
##### File: models/rectangle.py


3. Validate attributes
#### mandatory
#### Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded):

#### If the input is not an integer, raise the TypeError exception with the message: <name of the attribute> must be an integer. Example: width must be an integer
#### If width or height is under or equals 0, raise the ValueError exception with the message: <name of the attribute> must be > 0. Example: width must be > 0
#### If x or y is under 0, raise the ValueError exception with the message: <name of the attribute> must be >= 0. Example: x must be >= 0

``` shell
    guillaume@ubuntu:~/$ cat 2-main.py
    #!/usr/bin/python3
    """ 2-main """
    from models.rectangle import Rectangle

    if __name__ == "__main__":

        try:
            Rectangle(10, "2")
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))

        try:
            r = Rectangle(10, 2)
            r.width = -10
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))

        try:
            r = Rectangle(10, 2)
            r.x = {}
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))

        try:
            Rectangle(10, 2, 3, -1)
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))

    guillaume@ubuntu:~/$ ./2-main.py
    [TypeError] height must be an integer
    [ValueError] width must be > 0
    [TypeError] x must be an integer
    [ValueError] y must be >= 0
    guillaume@ubuntu:~/$ 
```
#### Repo:

##### GitHub repository: alx-higher_level_programming
##### Directory: 0x0C-python-almost_a_circle
##### File: models/rectangle.py


4. Area first
#### mandatory
#### Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.

```shell
    guillaume@ubuntu:~/$ cat 3-main.py
    #!/usr/bin/python3
    """ 3-main """
    from models.rectangle import Rectangle

    if __name__ == "__main__":

        r1 = Rectangle(3, 2)
        print(r1.area())

        r2 = Rectangle(2, 10)
        print(r2.area())

        r3 = Rectangle(8, 7, 0, 0, 12)
        print(r3.area())

    guillaume@ubuntu:~/$ ./3-main.py
    6
    20
    56
    guillaume@ubuntu:~/$ 
```
#### Repo:

##### GitHub repository: alx-higher_level_programming
##### Directory: 0x0C-python-almost_a_circle
##### File: models/rectangle.py


