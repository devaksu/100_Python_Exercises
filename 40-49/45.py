"""
Question:
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
"""

list45 = [1,2,3,4,5,6,7,8,9,10]

def square(n:int) -> int:
    return n**2


def func45(lista:list[int]):
    even = list(filter(lambda x: x % 2 == 0, lista))
    squares = list(map(square, even))
    print(squares)


func45(list45)