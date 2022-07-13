"""
Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

"""

max_val = int(input("Please give a maximum value of n: "))

def calc(n:int):
    i = 1
    sum = 0
    while i <= n:
        out = i/(i+1)
        sum += out
        i +=1
    
    print(f'Output: {sum:.2f}')

calc(max_val)