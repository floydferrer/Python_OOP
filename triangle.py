from math import sqrt
from random import randint

class Triangle:
    """
    A class used to represent a right triangle

    Attributes
    --------------

    a: int
        length of side a
    b: int
        length of side b
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f"Triangle(a={self.a}, b= {self.b})"
    
    def __str__(self):
        return f"I am a triangle with sides: {self.a} & {self.b}."

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    @classmethod
    def random(cls):
        """Class method which returns Triangle with random sides"""
        return cls(randint(1, 20), randint(1, 20))
    def get_hypotenuse(self):
        """Calculates hypotenuse (3rd side or right triangle)"""
        return sqrt(self.a **2 + self.b **2)

    def get_area(self):
        """Calculates area of right triangle"""
        return self.a * self.b /2

    def describe(self):
        """returns string representing right triangle"""
        return f"I am a triangle with sides: {self.a} & {self.b}."
