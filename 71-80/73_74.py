"""
Question73:
Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.

Question74:
Please write a program to randomly generate a list with 5 odd numbers between 100 and 200 inclusive.

Question75:
Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.
"""

import random
from math import lcm

def func73(lower:int, upper:int):
    if lower == upper:
        raise ValueError("Upper must be bigger than lower limit")

    else:
        if lower > upper:
            lower,upper =upper,lower

        random_list = [random.randint(lower,upper) for _ in range(5)]
        print(f'func73: {random_list}')

def func74(lower:int, upper:int):
    random_list = []
    if lower == upper:
        raise ValueError("Upper must be bigger than lower limit")

    if lower > upper:
        lower,upper = upper,lower
    
    while len(random_list) < 5:
        r = random.randint(lower,upper)
        if r % 2 == 1:
            random_list.append(r)
    
    print(f'func74: {random_list}')

def func75(lower:int, upper:int, divider1:int=5, divider2:int=7):
    random_list = []
    pyj = lcm(divider1,divider2)
    
    if lower == upper:
        raise ValueError("Upper must be bigger than lower limit")

    if lower > upper:
        lower,upper = upper,lower
    
    while len(random_list) < 5:
        r = random.randint(lower,upper)
        if r % pyj == 0:
            random_list.append(r)
    
    print(f'func75: {random_list}')
    

func73(100,200)
func74(100,200)
func75(1,1000)