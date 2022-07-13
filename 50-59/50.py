"""
Question:
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 

"""
from math import pi

class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def getArea(self):
        area = pi * (self.radius **2)
        print(f'Area: {area}')


c =Circle(5)
c.getArea()
