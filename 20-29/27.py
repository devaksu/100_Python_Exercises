"""
Question:
Define a function that can convert a integer into a string and print it in console.
"""

from re import S


def func(numero:int) -> str:
    s = str(numero)
    return s

print(func(10))
print(type(func(12)))