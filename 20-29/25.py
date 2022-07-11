"""
Question:
    Define a class, which have a class parameter and have a same instance parameter.
"""

class Person:
    name:str = ""

    def __init__(self, name:str = None):
        self.name = name

dev = Person('Aleksi')
print(dev.name)