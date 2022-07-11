"""
Question:
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
"""
list44 = [1,2,3,4,5,6,7,8,9,10]

def squares(n:int) -> int:
    return n**2

def func44(lista:list[int]) -> None:
    square = list(map(squares,lista))
    print(square)

func44(list44)