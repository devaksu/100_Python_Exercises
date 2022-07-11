"""
Question 46:
Write a program which can filter() to make a list whose elements are even number between a and b (both included).

Question 47:
Write a program which can map() to make a list whose elements are square of numbers between a and b (both included).
"""
list46 = [1,2,3,4,5,6,7,8,9,10]

# With list comprehension
def func46a(a:int, b:int) -> None:
    lista = [x for x in range(a,b+1) if x % 2 == 0]
    print(lista)

# With filter()
def func46b(lista:list[int]) -> None:
    even = list(filter(lambda x: x % 2 == 0,lista))
    print(even)


def func47(a:int, b:int) -> None:
    lista = [x for x in range(a, b+1)]
    squares = list(map(lambda x: x**2, lista))
    print(squares)

func46a(1,20)
func46b(list46)
func47(1,20)