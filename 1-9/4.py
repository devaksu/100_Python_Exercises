"""
Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""

from typing import Sequence


numbers = input("Please give number sequence: " )

def make_list(n: Sequence):
    # List using map-function
    generated_list = list(map(str, n.split(",")))
    print(generated_list)


def make_list_no_map(n: Sequence):
    # List without using map-function
    generated_list = list(n.split(","))
    print(generated_list)


def make_tuple(n: Sequence):
    # Tuple using map-function
    generated_tuple = tuple(map(str,n.split(",")))
    print(generated_tuple)


def make_tuple_no_map(n: Sequence):
    # Tuple without using map-function
    generated_tuple = tuple(n.split(","))
    print(generated_tuple)


make_list(numbers)
make_list_no_map(numbers)
make_tuple(numbers)
make_tuple_no_map(numbers)
