"""
Question71:
Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

Question72:
Please write a program to output a random number, which is divisible by 5 and 7 using random module and list comprehension.
"""

import random
from math import lcm

def func71(max_val:int):
    random_list = [n for n in range(max_val) if n % 2 == 0]
    random_number = random.choice(random_list)
    print(random_number)

def func72(n1:int, n2:int, max_val:int):
    pyj = lcm(n1,n2)
    if max_val < pyj:
        raise ValueError("Maximum value too small")
    else:
        random_list = [n for n in range(max_val) if n % pyj == 0]
        random_number = random.choice(random_list)
        print(random_number)


func71(101)
func72(5,7,25)