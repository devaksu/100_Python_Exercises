"""
Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].
"""

my_list = [5,6,77,45,22,12,24]

def func79(lista:list[int])-> list[int]:
    evens = [i for i in lista if i % 2 == 1]
    print(evens)

func79(my_list)