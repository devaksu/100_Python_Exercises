"""
Question 32:
Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) 
and the values are square of keys.


Question 33:
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) 
and the values are square of keys.

--> Question 32_33:
Define a function which can print a dictionary where the keys are numbers passed as arguments (both included) 
and the values are square of keys. The function should print both KEY AND VALUE

Question 34:
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) 
and the values are square of keys. The function should just print the VALUES ONLY.

Question 35:
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) 
and the values are square of keys. The function should just print the KEYS ONLY.

"""

def my_func32_33(a:int, b:int) -> dict[int]:
    my_dict = {}
    for i in range(a,b+1):
        my_dict[i] = i**2
    
    return my_dict

print(my_func32_33(2,8))
print('\n')

def my_func34_35(a:int, b:int) -> dict[int]:
    my_dict = {}
    for i in range(a,b+1):
        my_dict[i] = i**2
    print(f'Keys: {",".join(map(str,my_dict.keys()))}')
    print(f'Values: {",".join(map(str,my_dict.values()))}')

my_func34_35(2,8)