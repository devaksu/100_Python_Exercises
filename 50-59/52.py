"""
Define a class named Shape and its subclass Square. 
The Square class has an init function which takes a length as argument. 
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
"""

from operator import le


class Shape:
    def __init__(self):
        self.area = 0

    def getArea(self):
        print(self.area)

class Square(Shape):
    
    def __init__(self,length:int=1):
        self.length = length

    def getArea(self):
        area = self.length**2
        print(area)

s = Square()
s2 = Square(2)
s3 = Square(3)
s.getArea()
s2.getArea()
s3.getArea()