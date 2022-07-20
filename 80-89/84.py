"""
Question:
With a given list [12,24,35,24,88,120,155,88,120,175,155], 
write a program to print this list after removing all duplicate values 
with original order reserved.
"""

my_list = [12,24,35,24,88,175,120,155,88,120,155]
# With builtin functions
def cleaner_a(lista:list) -> list:
    cleaned_list = list(set(lista))
    cleaned_list.reverse()
    return cleaned_list


# Barebones
def cleaner_b(lista:list) -> list:
    cleaned = []
    for i in range(len(lista)):
        if lista[i] not in cleaned:
            cleaned.append(lista[i])
    
    reversed_list = cleaned[::-1]
    return reversed_list


# List comprehension
def cleaner_c(lista:list) -> list:
    cleaned = []
    [cleaned.append(i) for i in lista if i not in cleaned]
    
    reversed_list = cleaned[::-1]
    return reversed_list


print(cleaner_a(my_list))
print(cleaner_b(my_list))
print(cleaner_c(my_list))