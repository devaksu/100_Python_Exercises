"""
Please write a program which accepts basic mathematic expression from console and print the evaluation result.

Example:
If the following string is given as input to the program: 35+3

Then, the output of the program should be: 38
"""

expression = input("Please give mathematical expression: ")

def evaluate(expression:str) -> int:
    outcome = eval(expression)
    return outcome

print(evaluate(expression))