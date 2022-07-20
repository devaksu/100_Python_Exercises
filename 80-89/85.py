"""
Question:

Define a class Person and its two child classes: Male and Female. 
All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
"""

class Person():

    def __init__(self):
        self.gender = None
    
    def getGender(self):
        print(self.gender)

class Man(Person):
    
    def __init__(self):
        super().__init__()
        self.gender = "Male"
        

class Woman(Person):
    
    def __init__(self):
        super().__init__()
        self.gender = "Female"

m = Man().getGender()
w = Woman().getGender()
p = Person().getGender()

    
