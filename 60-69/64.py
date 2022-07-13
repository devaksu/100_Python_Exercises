"""
Question:

Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program: 10

Then, the output of the program should be: 0,2,4,6,8,10
"""
from typing import Generator

# List comprehension
def evens(max_val:int) -> None:
    even = [x for x in range(max_val+1) if x % 2 == 0]
    even = map(str,even)
    print(','.join(even))

# Yield
def even_generator(max_val:int) -> Generator[int, None, None]:
    x = 0
    while x <= max_val:
        if x % 2 == 0:
            yield x
        x += 1


def main():
    evens(10)

    eg = even_generator(10)
    values = []
    for i in eg:
        values.append(str(i))

    print(','.join(values))

if __name__ == '__main__':
    main()
