"""
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8
Then, the output should be: 40320
"""

from math import factorial

# With built-in functions
number = int(input("Please give a number to factorize: "))

def kertoma1(n:int):
    print(f'Kertoma1: {factorial(n)}')
    
#Without built-ins
def kertoma2(n:int):
    if n == 1:
        print(1)
    else:
        num = 1
        for i in range(2,n+1):
            num = i*num
        print(f'Kertoma2: {num}')

# With recursive fuunction call
def fact(n:int):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)

kertoma1(number)
kertoma2(number)
print(f'Kertoma3(fact): {fact(number)}')