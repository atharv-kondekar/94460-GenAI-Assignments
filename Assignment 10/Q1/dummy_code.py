# -----------------------------------------------------------
# Dummy Code Sample for Testing Code-Aware Chunking
# -----------------------------------------------------------

import os
import math

PI = 3.14159

def add(a, b):
    """Simple add function"""
    return a + b

def subtract(a, b):
    """Simple subtract function"""
    return a - b

def long_function():
    data = []
    for i in range(100):
        value = i * 2
        data.append(value)
    return data

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("Area not implemented")

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return PI * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, w, h):
        super().__init__("Rectangle")
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

def file_reader(path):
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        return f.read()

def spam():
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " * 20
    print(text)

# End of dummy code
