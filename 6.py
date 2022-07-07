"""
Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]

Following are the fixed values of C is 50 and H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.

Example
Let us assume the following comma separated input sequence is given to the program: 100,150,180
The output of the program should be: 18,22,24
"""
from math import sqrt

C = 50
H = 30

def func_q(D:list[int])-> None:
    result = []
    for value in D:
        Q = sqrt((2*C*value)/H)
        result.append(str(round(Q)))
    print(','.join(result))

D = [100,150,180]
func_q(D)