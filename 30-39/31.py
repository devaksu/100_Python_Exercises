"""
Question:
Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, 
otherwise print "It is an odd number".
"""

def my_func(number:int) -> None:
    if number % 2 == 0:
        print(f'Number {number} is even!')
        
    else:
        print(f'Number {number} is odd!')

my_func(11)
my_func(16)