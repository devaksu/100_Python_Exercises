"""
Please write assert statements to verify that every number in the list [2,4,6,8] is even.

"""

lista = [2,4,6,8]

def func66(lista:list[int]) -> bool:
    for i in lista:
        assert i % 2 == 0

func66(lista)