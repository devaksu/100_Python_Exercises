"""
Question:
By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.
"""
import numpy as np

# With list comprehension
def func82a(d1:int=3, d2:int=5, d3:int=8) -> list[list[list[int]]]:
    array = [[[0 for _ in range(d1)] for _ in range(d2)] for _ in range(d3)]
    return array


# With numpy
def func82b(d1:int=8, d2:int=5, d3:int=3) -> np.ndarray:
    array = np.zeros(shape=(d1,d2,d3))
    return array



print(func82a())
print(func82b())
