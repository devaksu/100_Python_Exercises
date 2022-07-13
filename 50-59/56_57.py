"""
Assuming that we have some email addresses in the "username@companyname.com" format, 
please write program to print the user name of a given email address. 
Both user names and company names are composed of letters only.

If the following email address is given as input to the program: john@google.com

Question 56:
Then, the output of the program should be: john

Question 57:
Then, the output of the program should be: google

In case of input data being supplied to the question, it should be assumed to be a console input.
"""

email=input("Please give me an email address: ")

def name_stripper(email:str) -> None:
    address = email.split("@")
    name56 = address[0]
    end57 = address[1].split('.')
    print(name56)
    print(end57[0])

name_stripper(email)