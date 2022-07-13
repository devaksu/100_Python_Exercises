"""
Question:
Define a class named Rectangle which can be constructed by a length and width. 
The Rectangle class has a method which can compute the area. 
"""

class Rectangle:
    def __init__(self, width:int=2, height:int=3):
        self.width = width
        self.height = height

    def getArea(self):
        print(f'Area: {(self.width*self.height)/2}')

r = Rectangle(6,5).getArea()
r2 = Rectangle()
r2.getArea()
