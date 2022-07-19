"""
Question69:
Please generate a random float where the value is between 10 and 100 using Python math module.

Question70:
Please generate a random float where the value is between 5 and 95 using Python math module.

"""

import random

def func69():
    random_float = (random.random())*100
    if random_float < 10:
        random_float +=10
    
    print(random_float)

def func70():
    random_float = (random.random())*95
    if random_float < 5:
        random_float +=5

    print(random_float)

func69()
func70()