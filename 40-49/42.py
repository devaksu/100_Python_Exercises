"""
Question:
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", 
otherwise print "No".
"""

def func42():
    string = input("Please give a word: ")
    string = string.upper()
    if string == "YES":
        print("Yes")
    else:
        print("No")

func42()