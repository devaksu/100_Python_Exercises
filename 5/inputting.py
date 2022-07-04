"""
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

"""

class Inputoutputstring:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Anna lause: ")
        return self.string

    
    def printString(self,string:str):
        self.string = string.upper()
        return self.string


