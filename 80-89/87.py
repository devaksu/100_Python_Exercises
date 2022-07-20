"""
Question:
Please write a program which prints permutations 1 -> n and prints them
"""
from itertools import permutations
from math import perm

# With math.perm()

def f87(n:int=3,k:int=2):
    """
    Select permutations sized k from population n
    """
    perm_count = perm(n,k)
    lista = [n for n in range(1,n+1)]
    perms = list(permutations(lista,k))
    print(f'Number of permutations: {perm_count}')
    print(perms)



f87()