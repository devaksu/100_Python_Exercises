"""
Question 36:
Define a function which can generate and print a list where the values are square of numbers between a and b (both included).

Question 37:
Define a function which can generate a list where the values are square of numbers between a and b (both included). 
Then the function needs to print the first 5 elements in the list.

Question 38:
Define a function which can generate a list where the values are square of numbers between a and b (both included). 
Then the function needs to print the last 5 elements in the list.

Question 39:
Define a function which can generate a list where the values are square of numbers between a and b (both included). 
Then the function needs to print all values except the first 5 elements in the list.
"""

def func36(a:int, b:int) -> list[int]:
    list36 = []
    for i in range(a,b+1):
        list36.append(i**2)

    return(list36)

def func37(a:int, b:int) -> list[int]:
    list37 = []
    for i in range(a,b+1):
        list37.append(i**2)

    return list37[:5]

def func38(a:int, b:int) -> list[int]:
    list38 = []
    for i in range(a,b+1):
        list38.append(i**2)

    return list38[-5:]

def func39(a:int, b:int) -> list[int]:
    list39 = []
    for i in range(a,b+1):
        list39.append(i**2)

    return list39[5:]

print(f'Func 36: \n{func36(1,20)}\n')
print(f'Func 37: \n{func37(1,20)}\n')
print(f'Func 38: \n{func38(1,20)}\n')
print(f'Func 39: \n{func39(1,20)}\n')