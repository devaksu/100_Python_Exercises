"""
Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program: 100

Then, the output of the program should be: 0,35,70
"""

from typing import Generator

def gene(max_val:int) -> Generator[int, None, None]:
    values = []
    for x in range(0,max_val+1):
         if x % 35 == 0:
            yield x
    
def main():        
    lista = gene(100)
    values = []
    for i in lista:
        values.append(str(i))
    print(','.join(values))

main()