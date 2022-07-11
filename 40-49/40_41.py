"""
Question 40:
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line 
and the last half values in one line. 


Question 41:
Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
"""

my_tuple = (1,2,3,4,5,6,7,8,9,10)

def func40(input_value:tuple[int]) -> None:
    first_half = ','.join(map(str,input_value[:5]))
    second_half = ','.join(map(str,input_value[5:]))
    print(f'First half: {first_half}')
    print(f'Second half: {second_half}')
    print('\n')

def func41(input_value:tuple[int]) -> None:
    even = [val for val in input_value if val % 2 == 0]
    odd = [val for val in input_value if val % 2 == 1]
    print(f'Evens: {",".join(map(str,even))}')
    print(f'Odds: {",".join(map(str,odd))}')

func40(my_tuple)
func41(my_tuple)