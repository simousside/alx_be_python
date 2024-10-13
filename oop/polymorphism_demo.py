import math


# Base class Shape
class Shape:
    # Method to be overridden by derived classes
    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")


# Derived class Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Override area method for rectangle
    def area(self):
        return self.length * self.width


# Derived class Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Override area method for circle
    def area(self):
        return math.pi * self.radius ** 2