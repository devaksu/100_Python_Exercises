"""
Question 48:
Define a class named American which has a static method called printNationality.

Question 49:
Define a class named American and its subclass NewYorker. 
"""

class American:
    @staticmethod
    def printNationality():
        print("American")

class NewYorker(American):
    pass

human = American()
human.printNationality()
#print(human.nationality)
