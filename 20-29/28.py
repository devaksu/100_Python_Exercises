"""
Question:
Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.
"""

def my_func(a:str,b:str) -> int:
    summa = int(a) + int(b)
    return summa

print(my_func('8', '2'))
