#!/usr/bin/python3
"""Define a Rectangle class"""

class Rectangle:
    """Represent a Rectangle"""
    def __init__(self, width =0, height =0):
        """Initializing a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new rectangle."""

            self.width = width
            self.height = height

            @property
            def width(self):
            """Get/set the width of a rectangle"""
            return self.__width

            @width.setter
            def width(self, value):
                if not isinstance(value, int):
                    raise TypeError("Width must be an integer")
                if value < 0
                raise ValueError("width must be >= 0")
            self.__width = value

            @property
            def height(self):
                """'Get/set the height of a rectangle"""
                return self.__height

            @hieght.setter
            def height(self, value):
                if not isinstance(value, int):
                    raise TypeError("Height must be an integer"):
                    if value < 0
                    raise ValueError("height must be >= 0")
                self.__height = value
