"""
Question:

With two given lists [1,3,6,78,35,55,12] and [12,24,35,24,88,120,155], 
write a program to make a list whose elements are intersection of the above given lists.
"""
my_list1 = [1,3,6,78,35,55,12]
my_list2 = [12,24,35,24,88,120,155]

def func83(lista1:list, lista2:list) -> list:
    intersection = [i for i in lista1 if i in lista2]
    return intersection

print(func83(my_list1, my_list2))