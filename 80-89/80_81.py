"""
Question80:
By using list comprehension, 
please write a program to print the list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

Question81:
By using list comprehension, please write a program to print the list 
after removing every second element in [12,24,35,70,88,120,155].
"""
import math
my_list = [12,24,35,70,88,120,155,800,801]
target = [24,70,120,800]

def func80(lista:list[int], div1:int=5, div2:int=7):
    pyj = math.lcm(div1,div2)
    deleted = [n for n in lista if n % pyj != 0]
    print(deleted)

def func81(lista:list[int]):
    t=0
    for _ in range(0, len(lista), 2):
        lista.pop(t)
        t += 1
    print(lista)

print(target)
func80(my_list)
func81(my_list)
