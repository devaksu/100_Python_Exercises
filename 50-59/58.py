"""
Question:

Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

Example:
If the following words is given as input to the program: 2 cats and 3 dogs.

Then, the output of the program should be:

['2', '3']

In case of input data being supplied to the question, it should be assumed to be a console input.
"""

# input_phrase = input("Please give an input phrase: ")
input_phrase = "2 cats and 3 dogs."

def func58(phrase:str)->list[str]:
    nums = []
    phrase = list(phrase)
    for a in phrase:
        if a.isdigit():
            nums.append(a)

    return nums

print(func58(input_phrase))